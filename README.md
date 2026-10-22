# ماشین حساب ساده

این پروژه یک ماشین حساب پایتونی برای چهار عمل اصلی است.

## استفاده

```python
from calculator import calculate

calculate(2, 3, "+")  # 5
calculate(8, 3, "-")  # 5
calculate(4, 3, "*")  # 12
calculate(9, 3, "/")  # 3.0
calculate(9, None, "sqrt")  # 3.0
```

عملگرهای پشتیبانی‌شده عبارت‌اند از `+`، `-`، `*`، `/` و `sqrt` (یا `√`) برای محاسبه جذر عملوند اول.
