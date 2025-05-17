import pandas as pd
import streamlit as st
from datetime import datetime

from grizly_app.ui.monitoring_state import MonitoringState
from grizly_app.utils.log_analyzer import LogAnalyzer


def show_log_dashboard():
    st.title("Health Monitoring")
    st.write("Real-time monitoring of application health and errors")

    # Initialize monitoring state
    if 'monitoring' not in st.session_state:
        st.session_state.monitoring = MonitoringState()

    # Add monitoring-specific CSS
    st.markdown("""
    <style>
    /* Monitoring dashboard specific styles */
    .monitoring-dashboard {
        font-family: 'Inter', sans-serif;
        color: #2E2E2E;
    }

    .monitoring-dashboard .stMetric {
        background-color: #FFFFFF;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        padding: 1rem;
    }

    .monitoring-dashboard .stPlotlyChart {
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .monitoring-dashboard .stDataFrame {
        background-color: #FFFFFF;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        padding: 1rem;
    }

    .monitoring-dashboard .stExpander {
        background-color: #FFFFFF !important;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        padding: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Initialize log analyzer
    analyzer = LogAnalyzer()

    # Time range filter in a collapsed container
    with st.expander("⚙️ Settings", expanded=False):
        st.session_state.monitoring.time_range = st.slider(
            "Time Range (hours)",
            min_value=1,
            max_value=24,
            value=st.session_state.monitoring.time_range,
            step=1
        )

    # Main metrics
    st.subheader("Overview")
    col1, col2, col3 = st.columns(3)

    with col1:
        error_count = len(analyzer.get_error_logs(st.session_state.monitoring.time_range))
        st.session_state.monitoring.update_metrics(
            error_count=error_count,
            app_logs_count=0,
            unique_errors=0
        )
        st.metric(
            "Total Errors",
            error_count,
            delta=(error_count - st.session_state.monitoring.prev_error_count)
        )
        st.session_state.monitoring.prev_error_count = error_count

    with col2:
        app_logs = analyzer.get_app_logs(st.session_state.monitoring.time_range)
        st.session_state.monitoring.update_metrics(
            error_count=0,
            app_logs_count=len(app_logs),
            unique_errors=0
        )
        st.metric(
            "Total Logs",
            len(app_logs),
            delta=len(app_logs) - st.session_state.monitoring.prev_app_logs_count
        )
        st.session_state.monitoring.prev_app_logs_count = len(app_logs)

    with col3:
        unique_errors = len({log['message'] for log in analyzer.get_error_logs(st.session_state.monitoring.time_range)})
        st.session_state.monitoring.update_metrics(
            error_count=0,
            app_logs_count=0,
            unique_errors=unique_errors
        )
        st.metric(
            "Unique Errors",
            unique_errors,
            delta=unique_errors - st.session_state.monitoring.prev_unique_errors
        )
        st.session_state.monitoring.prev_unique_errors = unique_errors

    # Recent Logs Table
    st.subheader("Recent Logs")
    try:
        recent_logs = analyzer.get_recent_logs()
        if recent_logs:
            # Add CSS styles for log entries
            st.markdown("""
            <style>
            .log-table {
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 1rem;
            }
            .log-row {
                display: table-row;
                border-bottom: 1px solid #dee2e6;
            }
            .log-cell {
                display: table-cell;
                padding: 12px;
                vertical-align: top;
                border-right: 1px solid #dee2e6;
            }
            .log-cell:last-child {
                border-right: none;
            }
            .log-timestamp {
                color: #6c757d;
                font-size: 0.9em;
                min-width: 160px;
                text-align: left;
            }
            .log-level {
                padding: 6px 12px;
                margin: 0;
                border: none;
                border-radius: 4px;
                font-size: 0.9em;
                cursor: default;
                pointer-events: none;
                font-weight: 500;
                text-align: left;
            }
            .log-level.green {
                background: #d4edda;
                color: #155724;
            }
            .log-level.orange {
                background: #fff3cd;
                color: #856404;
            }
            .log-level.red {
                background: #f8d7da;
                color: #721c24;
            }
            .log-message {
                text-align: left;
                color: #333;
                font-size: 0.9em;
                word-break: break-word;
            }
            </style>
            """, unsafe_allow_html=True)

            # Sort logs by timestamp
            sorted_logs = sorted(recent_logs, key=lambda x: x['timestamp'], reverse=True)
            
            # Display each log entry
            for log in sorted_logs:
                timestamp = datetime.fromisoformat(log['timestamp'])
                level = log['levelname']
                
                # Determine button color and emoji
                if level == 'ERROR':
                    button_class = 'red'
                    emoji = '❌'
                elif level == 'WARNING':
                    button_class = 'orange'
                    emoji = '⚠️'
                else:  # INFO
                    button_class = 'green'
                    emoji = '✅'
                
                # Format and display the log entry
                st.markdown(f"""
                <div class="log-table">
                    <div class="log-row">
                        <div class="log-cell">
                            <div class="log-timestamp">{timestamp.strftime('%Y-%m-%d %H:%M:%S')}</div>
                        </div>
                        <div class="log-cell">
                            <button class="log-level {button_class}">{emoji} {level}</button>
                        </div>
                        <div class="log-cell">
                            <div class="log-message">{log['message']}</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No logs available in the selected time range")
    except AttributeError as e:
        st.error(f"Error: LogAnalyzer missing get_recent_logs() method - {str(e)}")
    except (ValueError, TypeError) as e:
        st.error(f"Error processing logs: {str(e)}")
    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")
