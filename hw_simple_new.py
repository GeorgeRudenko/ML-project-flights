import marimo

__generated_with = "0.18.1"
app = marimo.App()


@app.cell
def _():
    # 1. Imports & Setup. Подключение библиотек и настройка окружения.

    import marimo as mo                 # Библиотека для веб-интерфейса
    import pandas as pd                 # Работа с таблицами
    import numpy as np                  # Математика
    import lightgbm as lgb              # ML-модель
    import matplotlib.pyplot as plt     # Графики
    from sklearn.model_selection import train_test_split # Разделение выборки
    import warnings

    # Отключаем технические предупреждения
    warnings.filterwarnings('ignore')
    return lgb, mo, pd, plt, train_test_split


@app.cell
def _(lgb, mo, pd, train_test_split):
    # 2. ML Pipeline: Loading & Training. Здесь мы загружаем данные, готовим признаки и обучаем модель. 

    @mo.cache
    def get_pipeline():
        """
        Загружает данные, выполняет Feature Engineering и обучает модель.
        """
        # 1. Загрузка данных
        try:
            df = pd.read_csv('flight_data_processed.csv')
        except FileNotFoundError:
            return None, None, None, None

        # 2. Признаки
        features = [
            'dep_time_min', 'distance', 'origin', 'day_of_month', 
            'day_of_week', 'month', 'dep_hour', 'origin_avg_delay', 
            'monthly_avg_delay', 'dow_avg_delay', 'hourly_avg_delay'
        ]
    
        # 3. Кодирование
        df['origin_encoded'] = df['origin'].astype('category').cat.codes
        origin_encoder = dict(zip(df['origin'], df['origin_encoded']))
    
        # 4. Сохранение исторических средних (Mean Encoding)
        maps = {
            'origin': df.groupby('origin')['origin_avg_delay'].mean().to_dict(),
            'hour': df.groupby('dep_hour')['hourly_avg_delay'].mean().to_dict()
        }

        X = df[features].copy()
        X['origin'] = df['origin_encoded']
        y = df['actual_arrival_min']

        # 5. Разделение на Train/Test
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=777, shuffle=True
        )

        # 6. Обучение модели
        model = lgb.LGBMRegressor(n_estimators=100, random_state=777, n_jobs=-1, verbose=-1)
        model.fit(X_train, y_train)
    
        return model, df, origin_encoder, maps

    # Запускаем пайплайн
    model, df, origin_encoder, maps = get_pipeline()
    return df, maps, model, origin_encoder


@app.cell
def _(df, mo):
    # 3. User Interface Controls. Элементы управления для бизнес-пользователя

    # Заголовок
    title = mo.md("# 🌪️ Weather Impact Simulator")

    # Выбор аэропорта
    if df is not None:
        all_airports = sorted(df['origin'].unique().tolist())
        airport_select = mo.ui.dropdown(all_airports, value='ORD', label="1. Origin Airport")
    else:
        airport_select = mo.md("⏳ Loading data...")

    # Слайдер Severity Factor
    severity_slider = mo.ui.slider(
        start=1.0, stop=3.0, step=0.1, value=1.0, 
        label="2. Weather Severity Factor (1.0 = Normal)"
    )

    # Вывод элементов
    mo.vstack([
        title,
        airport_select, 
        severity_slider
    ])
    return airport_select, severity_slider


@app.cell
def _(
    airport_select,
    maps,
    mo,
    model,
    origin_encoder,
    pd,
    plt,
    severity_slider,
):
    # 4. Computation Logic & Visualization. Расчет сценариев (Норма vs Стресс) и построение графика.

    # Создаем переменную для вывода
    final_output = mo.md("")

    # Проверяем, что модель загружена и аэропорт выбран
    if model is not None and airport_select.value:
    
        # --- 1. Подготовка данных (Typical Flight) ---
        dep_hour = 17
    
        # Строка-пример
        row = pd.DataFrame({
            'dep_time_min': [dep_hour * 60],
            'distance': [1000], 
            'origin': [origin_encoder[airport_select.value]], 
            'day_of_month': [15], 'day_of_week': [5], 'month': [2], 'dep_hour': [dep_hour],
            'origin_avg_delay': [maps['origin'].get(airport_select.value, 0)],
            'monthly_avg_delay': [0], 'dow_avg_delay': [0],
            'hourly_avg_delay': [maps['hour'].get(dep_hour, 0)]
        })

        # --- 2. Сценарий A: Normal Conditions ---
        pred_normal = model.predict(row)[0]
        duration_normal = pred_normal - (dep_hour * 60)

        # --- 3. Сценарий B: Stress Test ---
        row_stress = row.copy()
        # БИЗНЕС-ЛОГИКА: Умножаем исторические задержки на фактор слайдера
        row_stress['origin_avg_delay'] *= severity_slider.value
        row_stress['hourly_avg_delay'] *= severity_slider.value

        pred_stress = model.predict(row_stress)[0]
        duration_stress = pred_stress - (dep_hour * 60)

        # --- 4. Визуализация (Graph) ---
        fig, ax = plt.subplots(figsize=(8, 3))
    
        vals = [duration_normal, duration_stress]
        names = ["Normal Conditions", f"Forecast ({severity_slider.value}x)"]
        colors = ['#2ecc71', '#e74c3c' if severity_slider.value > 1.5 else '#f1c40f']

        ax.barh([0, 1], vals, color=colors, height=0.6)
        ax.set_yticks([0, 1])
        ax.set_yticklabels(names, fontweight='bold')
    
        ax.set_xlabel("Estimated Flight Duration (minutes)")
        ax.set_title(f"Weather Impact on Flight from {airport_select.value}")
    
        ax.set_xlim(0, max(vals) * 1.3)
        ax.grid(axis='x', linestyle='--', alpha=0.5)
    
        for i, v in enumerate(vals):
            ax.text(v + 3, i, f"{int(v)} min", va='center', fontweight='bold')

        # --- 5. Вывод (Output) ---
        delta = int(duration_stress - duration_normal)
    
        final_output = mo.vstack([
            mo.as_html(fig),
            mo.callout(
                mo.md(f"⏱ **Delay Risk:** Under current conditions ({severity_slider.value}x), flight time will increase by **{delta} minutes**."),
                kind="danger" if delta > 20 else "neutral"
            )
        ])
    else:
        final_output = mo.md("⏳ Loading model...")

    final_output
    return


if __name__ == "__main__":
    app.run()
