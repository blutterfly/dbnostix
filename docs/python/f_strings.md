# F Strings
Here’s a summary of the **5 Powerful F-String Tricks Every Python Developer Should Know** from the article:

---

### 🔑 Key Takeaways:

1. **Inline Expressions**
   F-strings allow evaluating expressions directly:

   ```python
   name = "John"
   age = 25
   print(f"{name} will be {age + 1} next year.")
   # Output: John will be 26 next year.
   ```

2. **Formatting Numbers**
   Easily control decimal places, commas, and percentages:

   ```python
   price = 49.98765
   print(f"Price: {price:.2f}")  # Output: Price: 49.99

   big_number = 1000000
   print(f"Formatted: {big_number:,}")  # Output: 1,000,000

   score = 0.8745
   print(f"Success rate: {score:.2%}")  # Output: 87.45%
   ```

3. **Debugging with `=`**
   Python 3.8+ supports variable name introspection inside f-strings:

   ```python
   x = 10
   y = 5
   print(f"{x=}, {y=}, {x + y=}")
   # Output: x=10, y=5, x + y=15
   ```

4. **Dynamic Formatting (Nesting F-Strings)**
   Use variables inside formatting specifiers:

   ```python
   width = 10
   number = 42.56789
   print(f"{number:.{width}f}")  # Output: 42.5678900000
   ```

5. **Multi-line F-Strings**
   Use f-strings with triple quotes for readable formatted blocks:

   ```python
   name = "John"
   age = 25
   city = "New York"

   info = f"""
   Name: {name}
   Age: {age}
   City: {city}
   """
   print(info)
   ```

---

