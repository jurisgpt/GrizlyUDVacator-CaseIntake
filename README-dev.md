
# 🧑‍💻 Grizly UD Vacator – Developer Layout Guide

This README documents how to work with the modular Streamlit UI system for the Grizly UD Vacator app. It is optimized for automation (Tony) and consistency across pages.

---

## ✅ Folder Structure

All UI components are modular and live in:

```
grizly_app/ui/
```

Each file contains one clear purpose: a header, component, or tab renderer.

---

## 📌 Core Files and Their Purpose

| File | Purpose | Called From |
|------|---------|-------------|
| `header.py` | App title block (centered) | `app.py` |
| `footer.py` | App footer text | `app.py` |
| `intake_header.py` | Header for intake form tab | `intake_form_tab.py` |
| `motion_header.py` | Header for motion tab | `motion_summary_tab.py` |
| `motion_components.py` | Buttons, download sections | `motion_summary_tab.py` |
| `decision_tree_header.py` | Decision tree section intro | `decision_tree_tab.py` |
| `legal_reasoning_header.py` | Header for legal logic tab | `legal_reasoning_tab.py` |
| `google_tabs_css.py` | Optional tab styling | `app.py` |

---

## 🧠 Layout Rule

- Set layout to `wide` globally in `app.py`
- Only center things like the app title using HTML in header modules
- Do **not** use `layout="centered"`

---

## 📌 Version Tags

- `v1.0.0-logic-locked`: First logic-stable milestone release
- `awareness-freeze-20250516`: Snapshot of complexity, coverage, and structure

---

## ✅ Usage Pattern

### In `app.py`:

```python
from ui.header import render_app_header
from ui.footer import render_footer

st.set_page_config(page_title="Tenant Relief Evaluation Tool", layout="wide")
render_app_header()
# tab logic...
render_footer()
```

### In `intake_form_tab.py`:

```python
from ui.intake_header import render_intake_intro
render_intake_intro()
# form logic...
```

---

## 🔍 Check Your Setup (Run These Commands)

1. ✅ Confirm current working directory:

```bash
pwd
```

2. ✅ List the UI directory contents:

```bash
ls -la grizly_app/ui/
```

3. ✅ Check Streamlit version:

```bash
pip show streamlit
```

4. ✅ Run the app to verify layout:

```bash
streamlit run grizly_app/app.py
```

---

## 📊 Project Awareness Map

Run the following to generate structure, complexity, and test coverage reports:

```bash
bash scripts/devtools/generate_project_map.sh
```

---

## ❓ Troubleshooting

| Symptom | Cause | Fix |
|--------|-------|-----|
| Title is centered but form is squished | `layout="centered"` was used | Change to `layout="wide"` |
| Layout broken in tab | Missing or bad HTML block | Check corresponding `*_header.py` file |
| Import error | Typos in file/module names | Use exact filenames from this README |

---

## 📌 Final Note

All headers, footers, and labeled sections must be declared via `render_*()` functions. Never hardcode layout or content into the tabs.

This architecture ensures scalability, clarity, and automation-readiness for both humans and machines 

View results in logs/awareness/<timestamp>/

