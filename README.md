# 🥗 **CookBot – Salad Recipes Dataset**

_A curated, cleaned dataset of salad recipes, designed for seamless integration into mobile apps and machine learning pipelines._

---

## 📝 **Description**

**CookBot – Salad Recipes Dataset** is a **targeted subset of the Food.com dataset**, focused exclusively on salad recipes. The primary goal of this dataset is to serve as a **lightweight and optimized data source** for integration into the **CookBot project**, which uses a **YOLOv12-based object detection model** to identify ingredients in real time.

We intentionally **filtered and reduced the original dataset** (~180,000 recipes and ~4,000 ingredients) down to ~800 **salad recipes** and ~30 **carefully standardized ingredients**. This was done to ensure:

- 🔍 **Efficient model training** on *all ingredients* without overwhelming computational resources,
- ⚡ **Smooth integration** into mobile apps with **SQLite support**,
- ✅ A dataset that's **clean, compact, and practical** for real-time AI applications.

**Cleaning & Curation Process:**

- ✅ Removed all rows with **missing values**
- ✅ **Standardized ingredient names** to avoid duplicates (e.g., "olive oil" vs "extra virgin olive oil")
- ✅ Ensured the data is **structured and convertible** between **CSV format** and **SQLite DB**
- ✅ Focused on **salads only**, filtering by recipe type and ingredient lists

---

## 🗂 **Table of Contents**

- [📁 Dataset Structure](#-dataset-structure)
- [⚙️ How to Use](#️-how-to-use)

---

## 📁 **Dataset Structure**

**File: `salad_recipes.csv`**

| **Column Name**   | **Description**                                                |
|-------------------|----------------------------------------------------------------|
| `name`            | Recipe title                                                   |
| `description`     | Recipe Description                                             |
| `ingredients`     | List of ingredients (comma-separated)                          |
| `steps`           | Step-by-step instructions                                      |
| `tags`            | Tags/keywords (e.g., vegan, gluten-free)                       |

---

## ⚙️ **How to Use**

This repository **not only provides functions that we created for the dataset filtering process**, but also contains **JupyterLab notebooks** that document the main steps used to:

- Filter and clean the original Food.com dataset,
- Standardize ingredient names,
- Remove missing values,
- Format the dataset for **CSV-to-SQLite** conversion.

**Important notes:**

- ✅ The notebook file  walks through the **filtering steps** applied **after isolating salad recipes**.
- ⚠️ **Initial preprocessing steps**—such as selecting salad recipes based on **tags** and **recipe names** from the full Food.com dataset—are **not included in this repo** but were part of the earlier transformation process.

---
