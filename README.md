# x5-retailhero-turicreate-baseline
turicreate baseline for https://retailhero.ai/c/recommender_system/overview

# Baseline задачи рекомендаций с библиотекой turicreate

## Как запускать?
1. Если совсем лень - [скачайте](https://drive.google.com/open?id=1aTGOSEDo1EuBpGkrKmSraykc9xKuLgLz) архив;
2. Если хочется свое, то:
  - клонируйте репозиторий
  - обучаете модель с помощью turicreate_baseline_model.ipynb модель
  - добавляете в архив папку с моделью, server.py, helpers.py, metadata.json
  - если нужно поменять докер - дейлайте свой образ
3. Для запуска используется свой образ с turicreate: artyerokhin/x5_contest_turi
4. Проверка точно такая же, как и в основном репозитории, только меняется образ docker на образ выше

## Каковы результаты?
1. локальная валидация:
  - average_precision_at_k: 0.088
  - average_normed_precision_at_k: 0.099
2. платформа:
  - check: 0.0907
  - public: 0.0754
