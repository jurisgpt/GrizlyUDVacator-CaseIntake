#!/bin/bash
source .venv/bin/activate
export PYTHONPATH=$PYTHONPATH:.
streamlit run streamlit_app.py --server.port 8501 --server.address localhost --browser.serverAddress localhost --browser.serverPort 8501 --logger.level debug
