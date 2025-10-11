import streamlit as st
import pandas as pd
import altair as alt
import datetime
import json
import time
import random
from datetime import datetime, timedelta
import io
import base64
import numpy as np

# ---------- CONFIGURAÇÕES AVANÇADAS ----------
st.set_page_config(
    page_title="BeSmart PRO - Sistema Inteligente de Seguros",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- THEME & STYLING ----------
def apply_custom_styles():
    st.markdown("""
    <style>
    /* Global Styles */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
        background-size: 20px 20px;
        animation: float 20s linear infinite;
    }
    
    @keyframes float {
        0% { transform: translate(0, 0) rotate(0deg); }
        100% { transform: translate(-20px, -20px) rotate(360deg); }
    }
    
    .metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 1.5rem;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border-left: 6px solid #667eea;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
        border: 1px solid rgba(255,255,255,0.2);
        backdrop-filter: blur(10px);
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    }
    
    .seguradora-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border-top: 6px solid;
        margin: 1rem 0;
        transition: all 0.3s ease;
        border: 1px solid rgba(255,255,255,0.2);
        backdrop-filter: blur(10px);
    }
    
    .seguradora-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
    }
    
    .progress-bar {
        height: 12px;
        background: linear-gradient(135deg, #e0e0e0 0%, #f5f5f5 100%);
        border-radius: 10px;
        margin: 15px 0;
        overflow: hidden;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
        border-radius: 10px;
        transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .progress-fill::after {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        animation: shimmer 2s infinite;
    }
    
    @keyframes shimmer {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    .faq-question {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        cursor: pointer;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .faq-question:hover {
        transform: translateX(10px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }
    
    .faq-answer {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        border-left: 6px solid #667eea;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    .download-section {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        text-align: center;
    }
    
    .coverage-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
        border-left: 6px solid;
        transition: all 0.3s ease;
    }
    
    .coverage-card:hover {
        transform: translateX(10px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }
    
    .coverage-feature {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .coverage-feature:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    .profile-checkbox {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        padding: 1.2rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        border-left: 6px solid #667eea;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    
    .profile-checkbox:hover {
        transform: translateX(5px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
    }
    
    .compatibility-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.9rem;
        display: inline-block;
        margin: 0.2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .profile-tag {
        background: linear-gradient(135deg, #00b09b 0%, #96c93d 100%);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.8rem;
        display: inline-block;
        margin: 0.1rem;
    }
    
    .section-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem 2rem;
        border-radius: 15px;
        margin: 2rem 0 1rem 0;
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
    
    .info-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 6px solid #667eea;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    }
    
    .success-card {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
    
    .warning-card {
        background: linear-gradient(135deg, #FF9800 0%, #F57C00 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
    
    .risk-card {
        background: linear-gradient(135deg, #dc3545 0%, #c82333 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
    
    /* Custom buttons */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.8rem 2rem;
        border-radius: 50px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .stButton button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
    }
    
    /* Input fields */
    .stTextInput input, .stNumberInput input, .stSelectbox select {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        padding: 0.8rem;
        transition: all 0.3s ease;
        font-size: 1rem;
    }
    
    .stTextInput input:focus, .stNumberInput input:focus, .stSelectbox select:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2);
    }
    
    /* Radio buttons */
    .stRadio > div {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        padding: 1rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    /* Success messages */
    .stSuccess {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 6px solid #2E7D32;
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
    
    /* Warning messages */
    .stWarning {
        background: linear-gradient(135deg, #FF9800 0%, #F57C00 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 6px solid #EF6C00;
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
    
    /* Info messages */
    .stInfo {
        background: linear-gradient(135deg, #2196F3 0%, #1976D2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 6px solid #0D47A1;
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
    
    /* Metric containers */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
    }
    
    /* Floating animation for cards */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .floating-card {
        animation: float 6s ease-in-out infinite;
    }
    
    /* Score bars */
    .score-bar-container {
        background: linear-gradient(135deg, #e0e0e0 0%, #f5f5f5 100%);
        height: 20px;
        border-radius: 10px;
        margin: 10px 0;
        overflow: hidden;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .score-bar-fill {
        height: 100%;
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
        border-radius: 10px;
        transition: width 0.8s ease;
        position: relative;
    }
    
    .score-bar-fill::after {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        animation: shimmer 2s infinite;
    }
    
    /* Text improvements */
    .main-title {
        font-size: 3.5rem;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, #FFD700, #FFFFFF, #87CEEB);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 2px 10px rgba(0,0,0,0.3);
        font-weight: 800;
    }
    
    .section-title {
        font-size: 2.2rem;
        color: #2c3e50;
        margin-bottom: 1.5rem;
        font-weight: 700;
    }
    
    .subsection-title {
        font-size: 1.6rem;
        color: #34495e;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    .card-title {
        font-size: 1.3rem;
        color: #2c3e50;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }
    
    .highlight-text {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 600;
    }
    
    /* Form improvements */
    .form-section {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }
    
    /* Dataframe improvements */
    .dataframe {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
    }
    
    /* Expander improvements */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        font-weight: 600;
    }
    
    /* Seguradora card improvements */
    .seguradora-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 1.5rem;
    }
    
    .seguradora-title {
        color: #2c3e50;
        margin: 0;
        font-size: 1.8rem;
    }
    
    .seguradora-subtitle {
        color: #666;
        margin: 0.5rem 0 0 0;
        font-size: 1rem;
        line-height: 1.4;
    }
    
    .match-badge {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 0.8rem 1.2rem;
        border-radius: 20px;
        font-weight: bold;
        font-size: 1.1rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        text-align: center;
    }
    
    .pontuacao-info {
        margin-top: 0.5rem;
        font-size: 0.9rem;
        color: #666;
        text-align: center;
    }
    
    .capital-total {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 2.5rem;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin: 2rem 0;
    }
    
    .capital-title {
        margin: 0 0 1.5rem 0;
        font-size: 1.8rem;
        font-weight: 600;
    }
    
    .capital-value {
        font-size: 3rem;
        font-weight: bold;
        margin: 0;
        text-shadow: 0 2px 10px rgba(0,0,0,0.3);
    }
    
    .capital-subtitle {
        margin: 1rem 0 0 0;
        opacity: 0.9;
        font-size: 1.1rem;
    }
    
    /* Coverage specific styles */
    .coverage-hero {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        position: relative;
        overflow: hidden;
    }
    
    .coverage-hero::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
        background-size: 30px 30px;
        animation: float 15s linear infinite;
    }
    
    .coverage-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .coverage-type-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border-top: 6px solid;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .coverage-type-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
    }
    
    .coverage-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    .coverage-badge {
        position: absolute;
        top: 1rem;
        right: 1rem;
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
    }
    
    .interactive-chart {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        margin: 2rem 0;
    }
    
    .coverage-comparison {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        margin: 2rem 0;
    }
    
    .protection-level {
        display: flex;
        align-items: center;
        margin: 1rem 0;
        padding: 1rem;
        background: rgba(102, 126, 234, 0.05);
        border-radius: 10px;
        border-left: 4px solid #667eea;
    }
    
    .protection-icon {
        font-size: 2rem;
        margin-right: 1rem;
        min-width: 60px;
        text-align: center;
    }
    
    .protection-details {
        flex: 1;
    }
    
    .protection-bar {
        height: 8px;
        background: #e0e0e0;
        border-radius: 4px;
        margin: 0.5rem 0;
        overflow: hidden;
    }
    
    .protection-fill {
        height: 100%;
        background: linear-gradient(90deg, #667eea, #764ba2);
        border-radius: 4px;
        transition: width 1s ease-in-out;
    }
    
    .coverage-detail-section {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        border-left: 6px solid #667eea;
    }
    
    /* Coverage Analysis Styles */
    .coverage-analysis-section {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        margin: 2rem 0;
    }
    
    .coverage-name {
        font-size: 1.4rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }
    
    .coverage-value {
        font-size: 1.8rem;
        font-weight: bold;
        color: #667eea;
        margin-bottom: 1rem;
    }
    
    .chart-container {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        margin: 2rem 0;
    }
    
    /* Detailed Coverage Card Styles */
    .detailed-coverage-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        margin: 2rem 0;
        border-left: 8px solid;
        border-right: 2px solid #f0f0f0;
        border-top: 2px solid #f0f0f0;
        border-bottom: 2px solid #f0f0f0;
    }
    
    .coverage-detail-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 2rem;
        padding-bottom: 1.5rem;
        border-bottom: 2px solid #f0f0f0;
    }
    
    .coverage-detail-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #2c3e50;
        margin: 0;
    }
    
    .coverage-detail-icon {
        font-size: 4rem;
        margin-right: 1.5rem;
    }
    
    .coverage-detail-value {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: right;
        margin: 0;
    }
    
    .detail-section {
        margin-bottom: 2rem;
    }
    
    .detail-section-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #667eea;
        display: inline-block;
    }
    
    .benefit-item {
        background: rgba(102, 126, 234, 0.05);
        padding: 1.2rem;
        border-radius: 12px;
        margin: 0.8rem 0;
        border-left: 4px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .benefit-item:hover {
        transform: translateX(5px);
        background: rgba(102, 126, 234, 0.1);
    }
    
    .tech-detail-row {
        display: flex;
        justify-content: space-between;
        padding: 1rem;
        border-bottom: 1px solid #f0f0f0;
        transition: all 0.3s ease;
    }
    
    .tech-detail-row:hover {
        background: rgba(102, 126, 234, 0.03);
    }
    
    .tech-detail-label {
        font-weight: 600;
        color: #2c3e50;
        flex: 1;
    }
    
    .tech-detail-value {
        font-weight: 500;
        color: #667eea;
        flex: 1;
        text-align: right;
    }
    
    /* Coverage Analysis Card - NOVO ESTILO */
    .coverage-analysis-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        margin: 1.5rem 0;
        border-left: 8px solid;
        transition: all 0.3s ease;
    }
    
    .coverage-analysis-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    }
    
    .coverage-analysis-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1.5rem;
    }
    
    .coverage-analysis-title {
        font-size: 1.6rem;
        font-weight: 700;
        color: #2c3e50;
        margin: 0;
    }
    
    .coverage-analysis-value {
        font-size: 2rem;
        font-weight: bold;
        color: #667eea;
        margin: 0;
    }
    
    .coverage-analysis-description {
        color: #666;
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }
    
    .coverage-analysis-features {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
        margin-bottom: 1.5rem;
    }
    
    .coverage-feature-item {
        background: rgba(102, 126, 234, 0.05);
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
    }
    
    .coverage-feature-title {
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }
    
    .coverage-feature-desc {
        color: #666;
        font-size: 0.9rem;
        line-height: 1.4;
    }
    </style>
    """, unsafe_allow_html=True)

apply_custom_styles()

# ---------- SESSION STATE INIT ----------
if 'cliente' not in st.session_state:
    st.session_state.cliente = {}
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'simulation_step' not in st.session_state:
    st.session_state.simulation_step = 0
if 'perfil_cliente' not in st.session_state:
    st.session_state.perfil_cliente = {}
if 'calculation_complete' not in st.session_state:
    st.session_state.calculation_complete = False
if 'selected_coverage' not in st.session_state:
    st.session_state.selected_coverage = None
if 'coverage_details_expanded' not in st.session_state:
    st.session_state.coverage_details_expanded = {}

# ---------- LISTA DE FILIAIS ----------
FILIAIS = [
    "BALNEARIO CAMBORIU",
    "BARRA MARAPENDI", 
    "BELEM",
    "BENTO GONCALVES",
    "BRUSQUE",
    "BX INVESTIMENTOS",
    "CAXIAS DO SUL",
    "DIRETORIA COMERCIAL REGIONAL 2",
    "FILIAL SUPER - EVANIO",
    "FLORIANOPOLIS",
    "IPANEMA",
    "JARDIM OCEANICO BARRA",
    "JURERE",
    "LAJEADO",
    "LEBLON",
    "LES GARS",
    "MANTO INVEST",
    "MARABA",
    "MINAS TRADE",
    "MOINHOS",
    "MONTES CLAROS",
    "NORTE RIO",
    "NOVA IGUACU",
    "PEDRA BRANCA",
    "PETROLINA",
    "PORTO ALEGRE",
    "QUANTOR INVEST",
    "RAJA",
    "RIO BARRA AMERICAS",
    "RJ – EAGLE ONE",
    "SAVASSI BH",
    "SAVASSI TERESINA",
    "TRES INVEST",
    "UBERLANDIA",
    "UNISUAM",
    "VOLTA REDOND",
    "GROWTH",
    "SMART OFFICE"
]

# ---------- BASE DE DADOS DE PERFIS E PESOS ----------
PERFIS_CLIENTE = [
    "Profissão com porte de armas",
    "70 anos + Doenças Graves", 
    "Só quer DIT",
    "Baixa renda",
    "Alta renda",
    "Pagamento Unico",
    "Resgate",
    "Jovem com filho pequeno",
    "85 anos",
    "Modular",
    "Só em vida",
    "Incluir pais",
    "Doenças Graves",
    "70 até 75",
    "Sucessão",
    "Autonomo",
    "Temporário",
    "Sucessão Empresarial",
    "Whole Life 80 anos"
]

# Pesos das seguradoras para cada perfil
PESOS_SEGURADORAS = {
    'Azos': {
        "Profissão com porte de armas": 100,
        "70 anos + Doenças Graves": 1,
        "Só quer DIT": 100,
        "Baixa renda": 2,
        "Alta renda": 1,
        "Pagamento Unico": 2,
        "Resgate": 1,
        "Jovem com filho pequeno": 1,
        "85 anos": 1,
        "Modular": 1,
        "Só em vida": 50,
        "Incluir pais": 1,
        "Doenças Graves": 1,
        "70 até 75": 5,
        "Sucessão": 0,
        "Autonomo": 1,
        "Temporário": 1,
        "Sucessão Empresarial": 1,
        "Whole Life 80 anos": 1
    },
    'Prudential': {
        "Profissão com porte de armas": 1,
        "70 anos + Doenças Graves": 100,
        "Sô quer DIT": 1,
        "Baixa renda": 1,
        "Alta renda": 2,
        "Pagamento Unico": 10,
        "Resgate": 1,
        "Jovem com filho pequeno": 1,
        "85 anos": 1,
        "Modular": 30,
        "Só em vida": 10,
        "Incluir pais": 1,
        "Doenças Graves": 2,
        "70 até 75": 5,
        "Sucessão": 1,
        "Autonomo": 1,
        "Temporário": 1,
        "Sucessão Empresarial": 1,
        "Whole Life 80 anos": 1
    },
    'Omint': {
        "Profissão com porte de armas": 1,
        "70 anos + Doenças Graves": 1,
        "Sô quer DIT": 1,
        "Baixa renda": 1,
        "Alta renda": 1,
        "Pagamento Unico": 4,
        "Resgate": 1,
        "Jovem com filho pequeno": 1,
        "85 anos": 1,
        "Modular": 30,
        "Só em vida": 1,
        "Incluir pais": 1,
        "Doenças Graves": 4,
        "70 até 75": 5,
        "Sucessão": 1,
        "Autonomo": 1,
        "Temporário": 33,
        "Sucessão Empresarial": 2,
        "Whole Life 80 anos": 1
    },
    'MAG Seguros': {
        "Profissão com porte de armas": 100,
        "70 anos + Doenças Graves": 1,
        "Só quer DIT": 100,
        "Baixa renda": 2,
        "Alta renda": 1,
        "Pagamento Unico": 10,
        "Resgate": 2,
        "Jovem com filho pequeno": 1,
        "85 anos": 100,
        "Modular": 1,
        "Só em vida": 50,
        "Incluir pais": 1,
        "Doenças Graves": 1,
        "70 até 75": 5,
        "Sucessão": 5,
        "Autonomo": 1,
        "Temporário": 1,
        "Sucessão Empresarial": 1,
        "Whole Life 80 anos": 100
    },
    'Icatu Seguros': {
        "Profissão com porte de armas": 1,
        "70 anos + Doenças Graves": 1,
        "Só quer DIT": 1,
        "Baixa renda": 2,
        "Alta renda": 1,
        "Pagamento Unico": 3,
        "Resgate": 1,
        "Jovem com filho pequeno": 1,
        "85 anos": 1,
        "Modular": 1,
        "Só em vida": 1,
        "Incluir pais": 100,
        "Doenças Graves": 1,
        "70 até 75": 5,
        "Sucessão": 1,
        "Autonomo": 1,
        "Temporário": 1,
        "Sucessão Empresarial": 1,
        "Whole Life 80 anos": 1
    },
    'MetLife': {
        "Profissão com porte de armas": 1,
        "70 anos + Doenças Graves": 1,
        "Só quer DIT": 1,
        "Baixa renda": 1,
        "Alta renda": 1,
        "Pagamento Unico": 5,
        "Resgate": 1,
        "Jovem com filho pequeno": 1,
        "85 anos": 1,
        "Modular": 30,
        "Só em vida": 1,
        "Incluir pais": 1,
        "Doenças Graves": 3,
        "70 até 75": 5,
        "Sucessão": 1,
        "Autonomo": 1,
        "Temporário": 1,
        "Sucessão Empresarial": 1,
        "Whole Life 80 anos": 1
    }
}

# ---------- SISTEMA DE CÁLCULO DE CAPITAL SEGURADO BASEADO NA TABELA ----------
class CalculadoraCapital:
    @staticmethod
    def calcular_cobertura_doencas_graves(cliente):
        """Calcula cobertura para doenças graves - 36x despesas mensais"""
        despesas_mensais = cliente.get('despesas_mensais', 0)
        despesas_filhos = cliente.get('despesas_filhos_mensais', 0)
        return (despesas_mensais) * 36
    
    @staticmethod
    def calcular_whole_life(cliente):
        """Calcula Whole Life - 20% do patrimônio imobilizado"""
        patrimonio = cliente.get('patrimonio_total', 0)
        return patrimonio * 0.20
    
    @staticmethod
    def calcular_term_life(cliente):
        """Calcula Term Life - Custo do filho x Anos até independência"""
        despesas_filhos = cliente.get('despesas_filhos_mensais', 0)
        anos_independencia = cliente.get('anos_ate_independencia', 0)
        return despesas_filhos * anos_independencia * 12
    
    @staticmethod
    def calcular_ipa(cliente):
        """Calcula Invalidez Permanente Total - Renda x 100"""
        renda_mensal = cliente.get('renda_mensal', 0)
        return renda_mensal * 100
    
    @staticmethod
    def calcular_dit_rit(cliente):
        """Calcula Diária por Incapacidade Temporária - Despesas/30"""
        despesas_mensais = cliente.get('despesas_mensais', 0)
        despesas_filhos = cliente.get('despesas_filhos_mensais', 0)
        despesas_totais = despesas_mensais
        return despesas_totais / 30
    
    @staticmethod
    def calcular_dih(cliente):
        """Calcula Diária por Internação Hospitalar - Despesas/30"""
        despesas_mensais = cliente.get('despesas_mensais', 0)
        despesas_filhos = cliente.get('despesas_filhos_mensais', 0)
        despesas_totais = despesas_mensais
        return despesas_totais / 30
    
    @staticmethod
    def calcular_capital_total(cliente):
        """Calcula o capital total segurado baseado em todas as coberturas"""
        coberturas = {
            'Doenças Graves': CalculadoraCapital.calcular_cobertura_doencas_graves(cliente),
            'Whole Life': CalculadoraCapital.calcular_whole_life(cliente),
            'Term Life': CalculadoraCapital.calcular_term_life(cliente),
            'Invalidez Permanente': CalculadoraCapital.calcular_ipa(cliente),
            'Diária Incapacidade Temporária': CalculadoraCapital.calcular_dit_rit(cliente),
            'Diária Internação Hospitalar': CalculadoraCapital.calcular_dih(cliente)
        }
        
        capital_total = sum(coberturas.values())
        
        return {
            'capital_total': capital_total,
            'coberturas_detalhadas': coberturas,
            'detalhes_calculo': coberturas
        }

# ---------- SISTEMA DE RECOMENDAÇÃO POR PERFIL ----------
class SistemaRecomendacao:
    @staticmethod
    def calcular_score_seguradoras(perfil_cliente):
        """Calcula o score de cada seguradora baseado no perfil do cliente"""
        scores = {}
        
        for seguradora, pesos in PESOS_SEGURADORAS.items():
            score_total = 0
            detalhes = {}
            perfis_compatíveis = []
            
            for perfil, ativo in perfil_cliente.items():
                if ativo:
                    peso = pesos.get(perfil, 1)
                    score_total += peso
                    detalhes[perfil] = peso
                    if peso >= 50:
                        perfis_compatíveis.append(perfil)
            
            max_possible_score = sum(pesos.get(p, 1) for p in perfil_cliente if perfil_cliente[p])
            porcentagem = (score_total / max_possible_score * 100) if max_possible_score > 0 else 0
            
            scores[seguradora] = {
                'score_total': score_total,
                'porcentagem_compatibilidade': min(100, porcentagem),
                'detalhes': detalhes,
                'perfis_compatíveis': perfis_compatíveis,
                'max_possible_score': max_possible_score
            }
        
        return scores
    
    @staticmethod
    def recomendar_melhores_seguradoras(perfil_cliente):
        """Retorna as 3 melhores seguradoras para o perfil"""
        scores = SistemaRecomendacao.calcular_score_seguradoras(perfil_cliente)
        
        seguradoras_ordenadas = sorted(
            scores.items(), 
            key=lambda x: x[1]['score_total'], 
            reverse=True
        )
        
        melhores = []
        for i, (seguradora, dados) in enumerate(seguradoras_ordenadas[:3]):
            melhores.append({
                'posicao': i + 1,
                'seguradora': seguradora,
                'score': dados['score_total'],
                'porcentagem': dados['porcentagem_compatibilidade'],
                'detalhes': dados['detalhes'],
                'perfis_compatíveis': dados['perfis_compatíveis']
            })
        
        return melhores

# ---------- SEGURADORAS OFICIAIS BESMART ----------
SEGURADORAS_BESMART = {
    "Azos": {
        "pontuacao": 8.5,
        "especialidade": ["Porte de Armas", "Profissões de Risco", "DIT"],
        "vantagens": ["Aceita porte de armas", "Cobertura DIT ampla", "Perfis especiais"],
        "cor": "#7C3AED",
        "tempo_aprovacao": "24h",
        "rating": "A",
        "preco_medio": "R$ 89,90",
        "perfil_ideal": "Profissionais com porte de armas e busca por DIT"
    },
    "Prudential": {
        "pontuacao": 9.0,
        "especialidade": ["Doenças Graves", "Planejamento Sucessório", "Alta Renda"],
        "vantagens": ["Cobertura ampliada doenças graves", "Solução sucessória", "Produtos modulares"],
        "cor": "#1E40AF",
        "tempo_aprovacao": "48h",
        "rating": "AA+",
        "preco_medio": "R$ 199,90",
        "perfil_ideal": "Clientes com foco em proteção contra doenças graves e sucessão"
    },
    "Omint": {
        "pontuacao": 9.4,
        "especialidade": ["Alta Renda", "Executivos", "Saúde Premium"],
        "vantagens": ["Rede médica exclusiva", "Atendimento concierge", "Cobertura internacional", "Hospitais premium"],
        "cor": "#FF6B35",
        "tempo_aprovacao": "24-72h",
        "rating": "AAA",
        "preco_medio": "R$ 299+",
        "perfil_ideal": "Executivos de alta renda que buscam saúde premium e atendimento diferenciado"
    },
    "MAG Seguros": {
        "pontuacao": 8.8,
        "especialidade": ["Servidores Públicos", "Classe Média", "Primeiro Seguro"],
        "vantagens": ["Preço competitivo", "Condições especiais servidores", "Baixa burocracia", "Pagamento flexível"],
        "cor": "#8A2BE2",
        "tempo_aprovacao": "24h",
        "rating": "A+",
        "preco_medio": "R$ 59,90",
        "perfil_ideal": "Servidores públicos e classe média buscando primeira proteção"
    },
    "Icatu Seguros": {
        "pontuacao": 9.1,
        "especialidade": ["Alta Renda", "Investidores", "Planejamento Sucessório"],
        "vantagens": ["Coberturas customizáveis", "Gestor dedicado", "Consultoria wealth", "Solução patrimonial"],
        "cor": "#00A859",
        "tempo_aprovacao": "48-72h",
        "rating": "AA+",
        "preco_medio": "R$ 189,90",
        "perfil_ideal": "Investidores e profissionais liberais com foco em proteção patrimonial"
    },
    "MetLife": {
        "pontuacao": 8.9,
        "especialidade": ["Multinacional", "Coletivos", "Grandes Empresas"],
        "vantagens": ["Atendimento global", "Soluções corporativas", "Rede ampla"],
        "cor": "#DC2626",
        "tempo_aprovacao": "72h",
        "rating": "AA",
        "preco_medio": "R$ 179,90",
        "perfil_ideal": "Funcionários de multinacionais e grandes corporações"
    }
}

# ---------- BASE DE DADOS DETALHADA DAS COBERTURAS ----------
COBERTURAS_DETALHADAS = {
    'Doenças Graves': {
        'icone': '🦠',
        'cor': '#FF6B6B',
        'descricao': 'Proteção financeira para tratamento de doenças graves como câncer, infarto, AVC, etc.',
        'beneficios': [
            'Capital para tratamento especializado',
            'Cobertura para 60+ doenças graves',
            'Pagamento em até 30 dias após diagnóstico',
            'Não precisa esperar alta hospitalar'
        ],
        'indicacao': 'Ideal para todos os perfis, especialmente acima de 40 anos',
        'valor_sugerido': '36x suas despesas mensais',
        'detalhes_tecnicos': {
            'Carência': '90 dias',
            'Coberturas Incluídas': 'Câncer, Infarto, AVC, Transplantes, etc.',
            'Limite Idade': '70 anos',
            'Renovação': 'Automática até 65 anos'
        }
    },
    'Whole Life': {
        'icone': '🏠',
        'cor': '#4ECDC4',
        'descricao': 'Proteção patrimonial que garante segurança financeira para sua família',
        'beneficios': [
            'Acumulo de valor em conta de participação',
            'Proteção vitalícia',
            'Resgate parcial disponível',
            'Excelente para planejamento sucessório'
        ],
        'indicacao': 'Perfis com patrimônio e planejamento familiar',
        'valor_sugerido': '20% do seu patrimônio total',
        'detalhes_tecnicos': {
            'Carência': '2 anos para suicídio',
            'Participação nos Lucros': 'Sim',
            'Resgate': 'Após 2 anos',
            'Forma Pagamento': 'Única ou parcelada'
        }
    },
    'Term Life': {
        'icone': '📚',
        'cor': '#45B7D1',
        'descricao': 'Proteção temporária focada em garantir educação e sustento dos filhos',
        'beneficios': [
            'Custo-benefício excelente',
            'Flexibilidade de prazo',
            'Cobertura ampla de causas',
            'Ideal para períodos específicos'
        ],
        'indicacao': 'Pais com filhos dependentes',
        'valor_sugerido': 'Despesas com filhos × anos até independência × 12',
        'detalhes_tecnicos': {
            'Carência': '30 dias para morte natural',
            'Prazos': '10, 15, 20, 30 anos',
            'Conversão': 'Para Whole Life sem médicos',
            'Cobertura': 'Morte por qualquer causa'
        }
    },
    'Invalidez Permanente': {
        'icone': '♿',
        'cor': '#96CEB4',
        'descricao': 'Proteção contra invalidez permanente por acidente ou doença',
        'beneficios': [
            'Cobertura total e parcial',
            'Isenção de pagamento após sinistro',
            'Reabilitação profissional',
            'Proteção mundial 24h'
        ],
        'indicacao': 'Todos os perfis, especialmente profissões de risco',
        'valor_sugerido': '100x sua renda mensal',
        'detalhes_tecnicos': {
            'Carência': '30 dias para doenças',
            'Grau Invalidez': 'A partir de 25%',
            'Idade Máxima': '65 anos',
            'Causas Cobertas': 'Acidentes e doenças'
        }
    },
    'Diária Incapacidade Temporária': {
        'icone': '💼',
        'cor': '#FECA57',
        'descricao': 'Proteção de renda durante períodos de incapacidade temporária para trabalho',
        'beneficios': [
            'Pagamento diário durante incapacidade',
            'Períodos curtos e longos',
            'Sem necessidade de internação',
            'Complemento ao INSS'
        ],
        'indicacao': 'Trabalhadores formais e informais',
        'valor_sugerido': 'Suas despesas mensais ÷ 30',
        'detalhes_tecnicos': {
            'Carência': '30 dias',
            'Prazo Máximo': '180 dias por evento',
            'Período Espera': '15 dias',
            'Limite Diário': 'Até R$ 1.000,00'
        }
    },
    'Diária Internação Hospitalar': {
        'icone': '🏥',
        'cor': '#FF9FF3',
        'descricao': 'Suporte financeiro durante internações hospitalares',
        'beneficios': [
            'Pagamento a partir do 1º dia',
            'Não precisa de DIT ativada',
            'Uso livre do valor',
            'Cobertura em qualquer hospital'
        ],
        'indicacao': 'Complementar ao plano de saúde',
        'valor_sugerido': 'Suas despesas mensais ÷ 30',
        'detalhes_tecnicos': {
            'Carência': '30 dias',
            'Limite Anual': '180 dias',
            'Internação Domiciliar': 'Coberta',
            'Doenças Pré-existentes': 'Após 2 anos'
        }
    }
}

# ---------- AI-POWERED FUNCTIONS ----------
class InsuranceAI:
    @staticmethod
    def generate_personalized_story(cliente):
        nome = cliente.get('nome', 'Cliente')
        idade = cliente.get('idade', 30)
        dependentes = cliente.get('dependentes', 0)
        renda_mensal = cliente.get('renda_mensal', 5000)
        capital_total = cliente.get('capital_sugerido', 0)
        
        calculo = CalculadoraCapital.calcular_capital_total(cliente)
        coberturas = calculo['coberturas_detalhadas']
        
        stories = {
            'familia': f"""
            **📖 Análise de Proteção da Família {nome}**
            
            Aos **{idade} anos**, {nome} é responsável por **{dependentes} dependente(s)** e possui uma **renda mensal de {formatar_moeda(renda_mensal)}**.
            
            **🛡️ Coberturas Calculadas:**
            - **Doenças Graves:** {formatar_moeda(coberturas['Doenças Graves'])} (36 meses de despesas)
            - **Proteção Patrimonial:** {formatar_moeda(coberturas['Whole Life'])} (20% do patrimônio)
            - **Educação dos Filhos:** {formatar_moeda(coberturas['Term Life'])} (custo até independência)
            - **Invalidez Permanente:** {formatar_moeda(coberturas['Invalidez Permanente'])} (100x a renda mensal)
            - **Proteção de Renda:** {formatar_moeda(coberturas['Diária Incapacidade Temporária'])}/dia
            - **Proteção Hospitalar:** {formatar_moeda(coberturas['Diária Internação Hospitalar'])}/dia
            
            **💡 Capital Total Recomendado:** **{formatar_moeda(capital_total)}**
            
            **🎯 Esta proteção garante que sua família mantenha o padrão de vida em qualquer cenário.**
            """,
            
            'profissional': f"""
            **🚀 Análise de Proteção Profissional de {nome}**
            
            Aos **{idade} anos**, {nome} está no auge da carreira com **renda de {formatar_moeda(renda_mensal)} mensais**.
            
            **🛡️ Coberturas Calculadas:**
            - **Doenças Graves:** {formatar_moeda(coberturas['Doenças Graves'])} (36 meses de despesas)
            - **Proteção Patrimonial:** {formatar_moeda(coberturas['Whole Life'])} (20% do patrimônio)
            - **Invalidez Permanente:** {formatar_moeda(coberturas['Invalidez Permanente'])} (100x a renda mensal)
            - **Proteção de Renda:** {formatar_moeda(coberturas['Diária Incapacidade Temporária'])}/dia
            - **Proteção Hospitalar:** {formatar_moeda(coberturas['Diária Internação Hospitalar'])}/dia
            
            **💡 Capital Total Recomendado:** **{formatar_moeda(capital_total)}**
            
            **💼 Sua carreira merece proteção inteligente e completa.**
            """
        }
        
        return stories['familia'] if dependentes > 0 else stories['profissional']
    
    @staticmethod
    def calculate_risk_score(cliente):
        score = 100
        idade = cliente.get('idade', 30)
        if idade > 50: score -= 20
        elif idade > 40: score -= 10
        
        if cliente.get('dependentes', 0) > 3: score -= 15
        
        profissoes_risco = ['piloto', 'bombeiro', 'militar', 'eletricista', 'construção']
        if any(risk in cliente.get('profissao', '').lower() for risk in profissoes_risco):
            score -= 25
            
        return max(30, score)
    
    @staticmethod
    def recommend_insurers(cliente, perfil_cliente):
        recommendations = []
        
        scores_perfil = SistemaRecomendacao.calcular_score_seguradoras(perfil_cliente)
        
        for nome, dados in SEGURADORAS_BESMART.items():
            score_base = dados['pontuacao']
            score_perfil = scores_perfil.get(nome, {}).get('score_total', 0) / 10
            
            score_final = (score_base * 0.6) + (score_perfil * 0.4)
            match_reasons = []
            
            renda_mensal = cliente.get('renda_mensal', 5000)
            idade = cliente.get('idade', 30)
            dependentes = cliente.get('dependentes', 0)
            profissao = cliente.get('profissao', '').lower()
            patrimonio = cliente.get('patrimonio_total', 0)
            
            if renda_mensal > 25000 and patrimonio > 500000 and "Alta Renda" in dados['especialidade']:
                score_final += 0.5
                match_reasons.append("💎 Perfil alta renda e patrimônio")
            elif 3000 <= renda_mensal <= 15000 and "Classe Média" in dados['especialidade']:
                score_final += 0.3
                match_reasons.append("🏠 Perfil classe média")
            
            if idade < 35 and "Jovens" in dados['especialidade']:
                score_final += 0.2
                match_reasons.append("🎯 Público jovem")
            elif idade > 45 and patrimonio > 300000 and "Planejamento Sucessório" in dados['especialidade']:
                score_final += 0.4
                match_reasons.append("📊 Perfil sucessório")
            
            if dependentes > 0 and "Famílias" in dados['especialidade']:
                score_final += 0.3
                match_reasons.append("👨‍👩‍👧‍👦 Perfil familiar")
            
            for perfil, ativo in perfil_cliente.items():
                if ativo and scores_perfil.get(nome, {}).get('detalhes', {}).get(perfil, 0) > 5:
                    match_reasons.append(f"✅ {perfil} (peso: {scores_perfil[nome]['detalhes'][perfil]})")
            
            porcentagem_compatibilidade = scores_perfil.get(nome, {}).get('porcentagem_compatibilidade', 0)
            
            recommendations.append({
                'Seguradora': nome,
                'Score': min(10, score_final),
                'Porcentagem_Compatibilidade': porcentagem_compatibilidade,
                'Pontuacao_Total': scores_perfil.get(nome, {}).get('score_total', 0),
                'Match': f"{min(100, int(score_final * 10))}%",
                'Especialidade': ', '.join(dados['especialidade']),
                'Preço Médio': dados['preco_medio'],
                'Tempo': dados['tempo_aprovacao'],
                'Perfil_Ideal': dados['perfil_ideal'],
                'Razões_Match': match_reasons,
                'Cor': dados['cor'],
                'Perfis_Compatíveis': scores_perfil.get(nome, {}).get('perfis_compatíveis', [])
            })
        
        recommendations.sort(key=lambda x: x['Score'], reverse=True)
        return recommendations

# ---------- FUNÇÕES PARA ANÁLISE DE COBERTURAS ----------
def create_coverage_hero(cliente, calculo):
    """Cria seção hero para análise de coberturas"""
    capital_total = calculo['capital_total']
    coberturas = calculo['coberturas_detalhadas']
    
    st.markdown(f"""
    <div class="coverage-hero">
        <h1 style="font-size: 3rem; margin-bottom: 1rem; font-weight: 800;">🛡️ Análise de Coberturas</h1>
        <p style="font-size: 1.5rem; margin-bottom: 2rem; opacity: 0.9;">Proteção Personalizada para {cliente.get('nome', 'Você')}</p>
    </div>
    """, unsafe_allow_html=True)

def create_coverage_comparison_chart(calculo):
    """Cria gráfico comparativo das coberturas usando Altair"""
    coberturas = calculo['coberturas_detalhadas']
    coberturas_validas = {k: v for k, v in coberturas.items() if v > 0}
    
    if not coberturas_validas:
        return
    
    df = pd.DataFrame({
        'Cobertura': list(coberturas_validas.keys()),
        'Valor': list(coberturas_validas.values())
    })
    
    # Gráfico de barras com Altair
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('Cobertura:N', title='', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Valor:Q', title='Valor (R$)'),
        color=alt.Color('Valor:Q', scale=alt.Scale(scheme='viridis'), legend=None),
        tooltip=['Cobertura', 'Valor']
    ).properties(
        title='📊 Distribuição do Capital por Cobertura',
        height=400
    ).configure_title(
        fontSize=20,
        color='#2c3e50'
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    ).configure_view(
        strokeWidth=0
    )
    
    st.altair_chart(chart, use_container_width=True)

def create_protection_level_analysis(cliente, calculo):
    """Cria análise dos níveis de proteção"""
    st.markdown("""
    <div class="interactive-chart">
        <h3 style="color: #2c3e50; margin-bottom: 2rem;">🎯 Níveis de Proteção da Sua Carteira</h3>
    """, unsafe_allow_html=True)
    
    coberturas = calculo['coberturas_detalhadas']
    capital_total = calculo['capital_total']
    
    niveis_protecao = [
        {
            'nome': '🦠 Saúde e Tratamento',
            'coberturas': ['Doenças Graves', 'Diária Internação Hospitalar'],
            'icone': '🏥',
            'descricao': 'Proteção contra custos médicos e tratamentos'
        },
        {
            'nome': '💼 Renda e Trabalho',
            'coberturas': ['Diária Incapacidade Temporária', 'Invalidez Permanente'],
            'icone': '💼',
            'descricao': 'Garantia de renda durante incapacidades'
        },
        {
            'nome': '🏠 Patrimônio e Família',
            'coberturas': ['Whole Life', 'Term Life'],
            'icone': '👨‍👩‍👧‍👦',
            'descricao': 'Proteção do patrimônio e futuro da família'
        }
    ]
    
    for nivel in niveis_protecao:
        valor_nivel = sum(coberturas.get(cobertura, 0) for cobertura in nivel['coberturas'])
        percentual = (valor_nivel / capital_total * 100) if capital_total > 0 else 0
        
        st.markdown(f"""
        <div class="protection-level">
            <div class="protection-icon">{nivel['icone']}</div>
            <div class="protection-details">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                    <h4 style="margin: 0; color: #2c3e50;">{nivel['nome']}</h4>
                    <span style="font-weight: bold; color: #667eea;">{percentual:.1f}%</span>
                </div>
                <p style="margin: 0 0 0.5rem 0; color: #666; font-size: 0.9rem;">{nivel['descricao']}</p>
                <div class="protection-bar">
                    <div class="protection-fill" style="width: {percentual}%;"></div>
                </div>
                <div style="font-size: 0.8rem; color: #999; margin-top: 0.5rem;">
                    {formatar_moeda(valor_nivel)} • {len([c for c in nivel['coberturas'] if coberturas.get(c, 0) > 0])} coberturas ativas
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def create_coverage_recommendations(cliente, calculo):
    """Cria recomendações personalizadas de cobertura"""
    st.markdown("""
    <div class="coverage-comparison">
        <h3 style="color: #2c3e50; margin-bottom: 2rem;">💡 Recomendações Inteligentes</h3>
    """, unsafe_allow_html=True)
    
    coberturas = calculo['coberturas_detalhadas']
    recomendacoes = []
    
    # Análise baseada no perfil do cliente
    idade = cliente.get('idade', 0)
    dependentes = cliente.get('dependentes', 0)
    renda = cliente.get('renda_mensal', 0)
    patrimonio = cliente.get('patrimonio_total', 0)
    
    if idade > 45 and coberturas['Doenças Graves'] == 0:
        recomendacoes.append({
            'tipo': '🦠 Doenças Graves',
            'prioridade': 'Alta',
            'motivo': 'A partir dos 45 anos, a probabilidade de doenças graves aumenta significativamente',
            'acao': 'Considere adicionar esta cobertura essencial'
        })
    
    if dependentes > 0 and coberturas['Term Life'] == 0:
        recomendacoes.append({
            'tipo': '📚 Term Life',
            'prioridade': 'Alta',
            'motivo': f'Você tem {dependentes} dependente(s) que precisam de proteção educacional',
            'acao': 'Essencial para garantir o futuro dos seus dependentes'
        })
    
    if patrimonio > 100000 and coberturas['Whole Life'] < patrimonio * 0.15:
        recomendacoes.append({
            'tipo': '🏠 Whole Life',
            'prioridade': 'Média',
            'motivo': f'Seu patrimônio de {formatar_moeda(patrimonio)} merece proteção adequada',
            'acao': 'Aumente para 20% do patrimônio para melhor proteção'
        })
    
    if renda > 0 and coberturas['Invalidez Permanente'] < renda * 80:
        recomendacoes.append({
            'tipo': '♿ Invalidez Permanente',
            'prioridade': 'Média',
            'motivo': 'Sua renda mensal precisa de proteção contra incapacidade',
            'acao': 'Recomendamos aumentar para 100x sua renda mensal'
        })
    
    if not recomendacoes:
        st.success("""
        **✅ Sua carteira está bem equilibrada!**
        
        Todas as coberturas essenciais para seu perfil estão adequadamente dimensionadas.
        """)
    else:
        for rec in recomendacoes:
            cor_prioridade = {
                'Alta': '#dc3545',
                'Média': '#ffc107',
                'Baixa': '#28a745'
            }[rec['prioridade']]
            
            st.markdown(f"""
            <div class="coverage-card" style="border-color: {cor_prioridade}">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
                    <h4 style="margin: 0; color: #2c3e50;">{rec['tipo']}</h4>
                    <span style="background: {cor_prioridade}; color: white; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8rem; font-weight: bold;">
                        Prioridade {rec['prioridade']}
                    </span>
                </div>
                <p style="color: #666; margin-bottom: 0.5rem; line-height: 1.5;">{rec['motivo']}</p>
                <p style="color: #2c3e50; font-weight: 500; margin: 0;">{rec['acao']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def show_detailed_coverage_card(cobertura_nome, dados_cobertura, valor_calculado, cliente):
    """Mostra card detalhado da cobertura quando clicar em Ver Detalhes"""
    
    st.markdown(f"""
    <div class="detailed-coverage-card" style="border-color: {dados_cobertura['cor']}">
        <div class="coverage-detail-header">
            <div style="display: flex; align-items: center;">
                <div class="coverage-detail-icon">{dados_cobertura['icone']}</div>
                <div>
                    <h1 class="coverage-detail-title">{cobertura_nome}</h1>
                    <p style="color: #666; font-size: 1.2rem; margin: 0.5rem 0 0 0;">{dados_cobertura['descricao']}</p>
                </div>
            </div>
            <div>
                <div class="coverage-detail-value" style="color: {dados_cobertura['cor']}">
                    {formatar_moeda(valor_calculado) if 'Diária' not in cobertura_nome else formatar_moeda(valor_calculado) + '/dia'}
                </div>
                <p style="color: #666; text-align: right; margin: 0.5rem 0 0 0;">Valor Calculado</p>
            </div>
        </div>
        
        
    """, unsafe_allow_html=True)
    
    for beneficio in dados_cobertura['beneficios']:
        st.markdown(f"""
        <div class="benefit-item">
            <div style="display: flex; align-items: center;">
                <span style="color: {dados_cobertura['cor']}; margin-right: 0.8rem; font-size: 1.2rem;">✓</span>
                <span style="font-weight: 500;">{beneficio}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
            </div>
            <div class="detail-section">
                <h3 class="detail-section-title">📋 Detalhes Técnicos</h3>
    """, unsafe_allow_html=True)
    
    for chave, valor in dados_cobertura['detalhes_tecnicos'].items():
        st.markdown(f"""
        <div class="tech-detail-row">
            <div class="tech-detail-label">{chave}</div>
            <div class="tech-detail-value">{valor}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Botões de ação
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button(f"🗂️ Simular {cobertura_nome}", key=f"simular_{cobertura_nome}", use_container_width=True):
            st.success(f"**Simulação iniciada para {cobertura_nome}!**")
    
    with col2:
        if st.button("📊 Comparar com Outras", key=f"comparar_{cobertura_nome}", use_container_width=True):
            st.info(f"**Comparando {cobertura_nome} com outras seguradoras...**")
    
    with col3:
        if st.button("❌ Fechar Detalhes", key=f"fechar_{cobertura_nome}", use_container_width=True):
            st.session_state.coverage_details_expanded[cobertura_nome] = False
            st.rerun()

# ---------- COMPONENTES ----------
def create_progress_tracker(step, total_steps=3):
    progress = (step / total_steps) * 100
    st.markdown(f"""
    <div class="progress-bar">
        <div class="progress-fill" style="width: {progress}%"></div>
    </div>
    <div style="display: flex; justify-content: space-between; font-size: 0.9rem; color: #666; margin-top: 0.5rem;">
        <span>{"✅" if step >= 1 else "⭕"} <strong>Cadastro</strong></span>
        <span>{"✅" if step >= 2 else "⭕"} <strong>Análise</strong></span>
        <span>{"✅" if step >= 3 else "⭕"} <strong>Resultado</strong></span>
    </div>
    """, unsafe_allow_html=True)

def create_insurer_card(seguradora, rank):
    cor = seguradora['Cor']
    
    perfis_badges = ""
    for perfil in seguradora.get('Perfis_Compatíveis', []):
        perfis_badges += f'<span class="profile-tag">{perfil}</span>'
    
    with st.container():
        st.markdown(f"""
        <div class="seguradora-card" style="border-color: {cor}">
            <div class="seguradora-header">
                <div>
                    <h3 class="seguradora-title">{seguradora['Seguradora']}</h3>
                    <p class="seguradora-subtitle">{seguradora['Perfil_Ideal']}</p>
                </div>
                <div>
                    <div class="match-badge">
                        #{rank} - {seguradora['Match']} Match
                    </div>
                    <div class="pontuacao-info">
                        <strong>Pontuação Total:</strong> {seguradora['Pontuacao_Total']} pts
                    </div>
                </div>
            </div>
            
            <div style="margin-bottom: 1.5rem;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                    <strong style="color: #2c3e50;">Compatibilidade:</strong>
                    <span style="color: #667eea; font-weight: bold;">{seguradora['Porcentagem_Compatibilidade']:.1f}%</span>
                </div>
                <div class="score-bar-container">
                    <div class="score-bar-fill" style="width: {seguradora['Porcentagem_Compatibilidade']}%;"></div>
                </div>
            </div>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1.5rem;">
                <div>
                    <strong style="color: #2c3e50;">📊 Especialidade:</strong><br>
                    <span style="color: #555; line-height: 1.4;">{seguradora['Especialidade']}</span>
                </div>
                <div>
                    <strong style="color: #2c3e50;">💰 Preço Médio:</strong> {seguradora['Preço Médio']}<br>
                    <strong style="color: #2c3e50;">⏱️ Aprovação:</strong> {seguradora['Tempo']}
                </div>
            </div>
            
            <div style="margin-top: 1rem;">
                <strong style="color: #2c3e50; display: block; margin-bottom: 0.5rem;">🎯 Perfis Compatíveis:</strong>
                {perfis_badges if perfis_badges else '<div style="color: #999; font-size: 0.9rem; padding: 0.5rem;">Nenhum perfil específico identificado</div>'}
            </div>
        </div>
        """, unsafe_allow_html=True)

def show_risk_analysis(cliente):
    """Mostra análise de riscos e necessidade do seguro"""
    idade = cliente.get('idade', 30)
    dependentes = cliente.get('dependentes', 0)
    renda_mensal = cliente.get('renda_mensal', 0)
    profissao = cliente.get('profissao', '')
    
    st.markdown('<div class="subsection-title">⚠️ Análise de Riscos e Necessidade</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="risk-card">
            <h4 style="margin: 0 0 1rem 0;">🚨 Riscos Identificados</h4>
        """, unsafe_allow_html=True)
        
        riscos = []
        
        if idade > 45:
            riscos.append(f"**👴 Idade ({idade} anos)**: Maior probabilidade de doenças graves")
        if dependentes > 0:
            riscos.append(f"**👨‍👩‍👧‍👦 {dependentes} dependente(s)**: Responsabilidade familiar aumentada")
        if renda_mensal > 0:
            riscos.append(f"**💰 Renda de {formatar_moeda(renda_mensal)}**: Necessidade de proteção de renda")
        
        profissoes_risco = {
            'construção': 'Risco de acidentes de trabalho',
            'motorista': 'Risco de acidentes de trânsito', 
            'eletricista': 'Risco de acidentes elétricos',
            'militar': 'Risco ocupacional elevado',
            'bombeiro': 'Alto risco profissional'
        }
        
        for risco, descricao in profissoes_risco.items():
            if risco in profissao.lower():
                riscos.append(f"**🏢 Profissão**: {descricao}")
        
        if not riscos:
            riscos.append("**✅ Perfil de risco moderado**")
        
        for risco in riscos:
            st.markdown(f"- {risco}", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h4 style="margin: 0 0 1rem 0; color: #2c3e50;">🛡️ Porque Você Precisa de Seguro</h4>
        """, unsafe_allow_html=True)
        
        beneficios = [
            "**💼 Proteção de Renda**: Garante sustento familiar em caso de incapacidade",
            "**🏥 Cobertura Hospitalar**: Custos com internação e tratamentos",
            "**📚 Educação dos Filhos**: Mantém estudos dos dependentes",
            "**🏠 Manutenção do Patrimônio**: Protege seu patrimônio conquistado",
            "**😌 Paz Espiritual**: Segurança para você e sua família",
            "**💰 Planejamento Sucessório**: Organização para as gerações futuras"
        ]
        
        for beneficio in beneficios:
            st.markdown(f"- {beneficio}", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

# ---------- FUNÇÕES BASE ----------
def formatar_moeda(valor: float) -> str:
    if valor == 0:
        return "R$ 0,00"
    return f"R$ {valor:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")

# ---------- FUNÇÕES DE DOWNLOAD ----------
def gerar_proposta_txt(cliente, seguradoras_recomendadas, melhores_seguradoras):
    """Gera uma proposta em formato TXT"""
    
    calculo = CalculadoraCapital.calcular_capital_total(cliente)
    coberturas = calculo['coberturas_detalhadas']
    
    proposta = f"""
============================================
PROPOSTA DE SEGURO DE VIDA - BESMART PRO
============================================

DADOS DO CLIENTE:
----------------
Nome: {cliente.get('nome', 'Não informado')}
Idade: {cliente.get('idade', 'Não informado')} anos
Profissão: {cliente.get('profissao', 'Não informado')}
Dependentes: {cliente.get('dependentes', 0)}
Renda Mensal: {formatar_moeda(cliente.get('renda_mensal', 0))}
Patrimônio: {formatar_moeda(cliente.get('patrimonio_total', 0))}
Filial: {cliente.get('filial', 'Não informado')}

PERFIL DO CLIENTE:
-----------------
"""
    
    perfis_ativos = [perfil for perfil, ativo in st.session_state.perfil_cliente.items() if ativo]
    if perfis_ativos:
        for perfil in perfis_ativos:
            proposta += f"- {perfil}\n"
    else:
        proposta += "- Nenhum perfil específico selecionado\n"
    
    proposta += f"""
DETALHAMENTO DAS COBERTURAS:
---------------------------
"""
    
    for cobertura, valor in coberturas.items():
        if valor > 0:
            if 'Diária' in cobertura:
                proposta += f"- {cobertura}: {formatar_moeda(valor)}/dia\n"
            else:
                proposta += f"- {cobertura}: {formatar_moeda(valor)}\n"
    
    proposta += f"""
CAPITAL TOTAL SUGERIDO: {formatar_moeda(calculo['capital_total'])}

MELHORES SEGURADORAS PARA SEU PERFIL:
------------------------------------
"""
    
    for melhor in melhores_seguradoras:
        proposta += f"""
{melhor['posicao']}. {melhor['seguradora']}
   - Score de Compatibilidade: {melhor['score']} pontos
   - Porcentagem: {melhor['porcentagem']:.1f}%
   - Perfis que mais contribuíram: {', '.join(list(melhor['detalhes'].keys())[:3])}
"""
    
    proposta += f"""
SEGURADORAS RECOMENDADAS:
-----------------------
"""
    
    for i, seguradora in enumerate(seguradoras_recomendadas[:3], 1):
        proposta += f"""
{i}. {seguradora['Seguradora']}
   - Compatibilidade: {seguradora['Match']}
   - Score: {seguradora['Score']}/10
   - Pontuação Total: {seguradora['Pontuacao_Total']} pontos
   - Porcentagem: {seguradora['Porcentagem_Compatibilidade']:.1f}%
   - Especialidade: {seguradora['Especialidade']}
   - Preço Médio: {seguradora['Preço Médio']}
"""
    
    proposta += f"""
DADOS DO ASSESSOR:
-----------------
Filial: {cliente.get('filial', 'Não informado')}
Assessor: {cliente.get('assessor', 'Não informado')}
Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}

============================================
BeSmart PRO - Parceiro Oficial
============================================
"""
    
    return proposta

def criar_download_button(data, filename, button_text, file_type):
    """Cria um botão de download"""
    
    if file_type == 'txt':
        b64 = base64.b64encode(data.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="{filename}" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 14px 28px; text-decoration: none; border-radius: 10px; display: inline-block; font-weight: bold; text-align: center; font-size: 1rem; box-shadow: 0 4px 15px rgba(0,0,0,0.2); transition: all 0.3s ease;">{button_text}</a>'
    elif file_type == 'csv':
        csv = data.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="{filename}" style="background: linear-gradient(135deg, #00b09b 0%, #96c93d 100%); color: white; padding: 14px 28px; text-decoration: none; border-radius: 10px; display: inline-block; font-weight: bold; text-align: center; font-size: 1rem; box-shadow: 0 4px 15px rgba(0,0,0,0.2); transition: all 0.3s ease;">{button_text}</a>'
    
    return href

# ---------- FAQ COMPLETO ----------
FAQ_COMPLETO = {
    "🧭 1. Conceitos Gerais e Funcionamento (1 – 30)": [
        {
            "pergunta": "O que é um seguro de vida?",
            "resposta": """
            **Seguro de Vida** é um contrato entre você (segurado) e uma seguradora, onde você paga prêmios periódicos em troca de proteção financeira para seus beneficiários em caso de:
            
            • **Morte** - Sua família recebe o capital segurado
            • **Invalidez** - Você recebe em caso de acidentes incapacitantes
            • **Doenças Graves** - Suporte financeiro para tratamentos
            
            É a **proteção mais importante** que você pode oferecer à sua família! 🛡️
            """,
            "destaque": "Proteção financeira familiar essencial"
        },
        {
            "pergunta": "Como funciona um seguro de vida?",
            "resposta": """
            **Funcionamento do Seguro de Vida:**
            
            1. **Contratação**: Você escolhe as coberturas e valores
            2. **Pagamento**: Paga prêmios mensais/anuais
            3. **Vigência**: A proteção está ativa enquanto pagar
            4. **Sinistro**: Em caso de evento coberto, aciona a seguradora
            5. **Indenização**: Beneficiários recebem o capital segurado
            
            **💡 É como um guarda-chuva: você espera nunca precisar, mas fica tranquilo sabendo que está protegido.**
            """,
            "destaque": "Proteção contínua em troca de pagamento periódico"
        },
        {
            "pergunta": "Qual a diferença entre seguro de vida e previdência privada?",
            "resposta": """
            **Principais Diferenças:**
            
            **🎯 Seguro de Vida:**
            • Foco em **proteção**
            • Indenização em caso de sinistro
            • Beneficiários recebem
            • Prazo determinado ou vitalício
            
            **💰 Previdência Privada:**
            • Foco em **acumulação**
            • Você recebe o valor
            • Para aposentadoria
            • Longo prazo com rentabilidade
            
            **💡 Ideal: Ter ambos para proteção completa!**
            """,
            "destaque": "Seguro protege, previdência acumula"
        },
        {
            "pergunta": "Qual a importância de ter um seguro de vida?",
            "resposta": """
            **Importância do Seguro de Vida:**
            
            • **Proteção Familiar**: Garante sustento dos dependentes
            • **Cobertura de Dívidas**: Evita herança de financiamentos
            • **Educação dos Filhos**: Assegura continuidade dos estudos
            • **Custos Finais**: Cobre despesas funerárias e médicas
            • **Planejamento Sucessório**: Organiza transferência patrimonial
            • **Tranquilidade**: Segurança psicológica e emocional
            
            **🎯 É um ato de amor e responsabilidade com quem você ama.**
            """,
            "destaque": "Proteção para quem depende de você"
        },
        {
            "pergunta": "Existe carência no seguro de vida?",
            "resposta": """
            **Sim, existe carência no seguro de vida:**
            
            • **Morte Natural**: 2 anos (em média)
            • **Morte Acidental**: 24 horas a 30 dias
            • **Doenças Graves**: 90 a 180 dias
            • **Invalidez**: 30 a 90 dias
            
            **💡 A carência é o período entre a contratação e o início da cobertura total.**
            
            **Importante**: Suicídio geralmente tem carência de 2 anos.
            """,
            "destaque": "Período de espera para cobertura total"
        },
        {
            "pergunta": "Qual a idade mínima para contratar?",
            "resposta": """
            **Idade Mínima para Contratar:**
            
            • **18 anos** - Maioridade civil
            • Algumas seguradoras aceitam a partir de **16 anos** com autorização dos pais
            • Para crianças, pais podem contratar a partir do **nascimento**
            
            **💡 Quanto mais cedo contratar, menores serão os prêmios!**
            """,
            "destaque": "A partir de 18 anos, ou 16 com autorização"
        },
        {
            "pergunta": "Qual a idade máxima para contratar?",
            "resposta": """
            **Idade Máxima para Contratação:**
            
            • **Seguro Temporário**: Até 70-75 anos
            • **Seguro Vitalício**: Até 80-85 anos
            • **Doenças Graves**: Até 60-65 anos
            
            **💡 A idade máxima varia por seguradora e tipo de cobertura.**
            
            **Dica**: Contrate enquanto é jovem para garantir melhores condições!
            """,
            "destaque": "Varia de 70 a 85 anos dependendo do produto"
        },
        {
            "pergunta": "Quem pode contratar um seguro de vida?",
            "resposta": """
            **Quem Pode Contratar:**
            
            • **Maiores de 18 anos** em pleno gozo de capacidade civil
            • **Estrangeiros** residentes no Brasil com documentação regular
            • **Pessoas físicas** de qualquer profissão (algumas com restrições)
            • **Empresas** para seguros coletivos de funcionários
            
            **💡 Basicamente qualquer pessoa que tenha interesse em proteger sua família ou patrimônio.**
            """,
            "destaque": "Maiores de 18 anos com capacidade civil"
        },
        {
            "pergunta": "Qual a duração do seguro?",
            "resposta": """
            **Duração do Seguro de Vida:**
            
            • **Temporário**: 1 a 30 anos (prazo determinado)
            • **Vitalício**: Até o falecimento (sem prazo)
            • **Resgatável**: 15+ anos (com valor de resgate)
            • **Anual**: Renovação anual
            
            **💡 Você escolhe a duração de acordo com suas necessidades!**
            
            **Exemplo**: Contrate até os filhos se formarem ou até a aposentadoria.
            """,
            "destaque": "De 1 ano até vitalício, conforme necessidade"
        },
        {
            "pergunta": "O seguro de vida tem validade no exterior?",
            "resposta": """
            **Validade no Exterior:**
            
            • **Morte e Invalidez**: Geralmente cobertura mundial
            • **Doenças Graves**: Pode ter restrições por país
            • **Assistências**: Podem ser apenas no Brasil
            
            **💡 Verifique sempre as condições específicas da apólice!**
            
            **Dica**: Se viaja muito, contrate cobertura internacional.
            """,
            "destaque": "Geralmente sim, mas verifique condições específicas"
        }
    ],
    "📝 2. Tipos e Modalidades de Seguro (31 – 60)": [
        {
            "pergunta": "Quais são os principais tipos de seguro de vida?",
            "resposta": """
            **Principais Tipos de Seguro de Vida:**
            
            • **Temporário**: Proteção por prazo determinado
            • **Vitalício**: Proteção por toda a vida
            • **Resgatável**: Combina proteção com investimento
            • **Universal**: Flexibilidade de prêmios e coberturas
            • **Coletivo**: Para grupos (empresas, associações)
            • **Acidentes Pessoais**: Foco em acidentes
            
            **💡 Cada tipo atende a uma necessidade específica!**
            """,
            "destaque": "Temporário, vitalício, resgatável, universal e coletivo"
        },
        {
            "pergunta": "O que é seguro temporário?",
            "resposta": """
            **Seguro Temporário:**
            
            • **Proteção por prazo determinado** (ex: 10, 20, 30 anos)
            • **Mais barato** que o vitalício
            • **Ideal** para períodos específicos (filhos na escola, financiamento)
            • **Sem valor de resgate** (puro risco)
            
            **💡 Perfeito para quem precisa de proteção por um período específico!**
            
            **Exemplo**: Até os filhos se formarem na faculdade.
            """,
            "destaque": "Proteção por prazo determinado, mais econômico"
        },
        {
            "pergunta": "O que é seguro vitalício?",
            "resposta": """
            **Seguro Vitalício:**
            
            • **Proteção por toda a vida**
            • **Prêmios geralmente mais altos**
            • **Garantia** de que os beneficiários sempre receberão
            • **Excelente** para planejamento sucessório
            
            **💡 Ideal para quem quer garantir que a família receba independentemente de quando falecer!**
            """,
            "destaque": "Proteção vitalícia, ideal para sucessão"
        },
        {
            "pergunta": "O que é seguro de vida resgatável?",
            "resposta": """
            **Seguro Resgatável:**
            
            • **Combina proteção com poupança**
            • **Acumula valor** em conta de participação
            • **Pode resgatar** após período de carência
            • **Prêmios mais altos** que o temporário
            
            **💡 Protege sua família e ajuda a construir patrimônio!**
            
            **Funciona como**: Seguro + investimento de longo prazo.
            """,
            "destaque": "Combina proteção com acumulação de patrimônio"
        },
        {
            "pergunta": "O que é seguro universal?",
            "resposta": """
            **Seguro Universal:**
            
            • **Máxima flexibilidade** de prêmios e coberturas
            • **Pode ajustar** valores conforme necessidade
            • **Componente de investimento**
            • **Transparência** total dos custos
            
            **💡 Para quem quer controle total sobre o seguro!**
            
            **Vantagem**: Adapta-se às mudanças da sua vida.
            """,
            "destaque": "Máxima flexibilidade em prêmios e coberturas"
        }
    ],
    "💰 3. Coberturas e Benefícios (61 – 100)": [
        {
            "pergunta": "Quais são as coberturas básicas?",
            "resposta": """
            **Coberturas Básicas do Seguro de Vida:**
            
            • **Morte por qualquer causa** (natural ou acidental)
            • **Invalidez Permanente** por acidente
            • **Doenças Graves** (câncer, infarto, AVC)
            • **Diária por Incapacidade Temporária** (DIT)
            • **Diária por Internação Hospitalar** (DIH)
            
            **💡 Estas são as coberturas essenciais para proteção completa!**
            """,
            "destaque": "Morte, invalidez, doenças graves, DIT e DIH"
        },
        {
            "pergunta": "Quais são as coberturas adicionais mais comuns?",
            "resposta": """
            **Coberturas Adicionais Mais Comuns:**
            
            • **Invalidez Funcional** por doença
            • **Transplante de Órgãos**
            • **Assistência Funeral**
            • **Despesas Médicas**
            • **Proteção Financeira**
            • **Cesta Básica Familiar**
            
            **💡 Personalize seu seguro conforme suas necessidades específicas!**
            """,
            "destaque": "Diversas opções para personalização completa"
        },
        {
            "pergunta": "O que é cobertura por morte natural?",
            "resposta": """
            **Cobertura por Morte Natural:**
            
            • **Proteção** contra morte por causas naturais
            • **Doenças**, idade avançada, condições crônicas
            • **Carência** geralmente de 2 anos
            • **Capital** pago aos beneficiários
            
            **💡 Garante que sua família receba mesmo se falecer por causas naturais!**
            """,
            "destaque": "Proteção contra morte por causas naturais"
        },
        {
            "pergunta": "O que é cobertura por morte acidental?",
            "resposta": """
            **Cobertura por Morte Acidental:**
            
            • **Proteção** contra morte por acidentes
            • **Trânsito**, quedas, afogamento, etc.
            • **Carência** geralmente de 24h a 30 dias
            • **Capital** geralmente dobrado ou triplicado
            
            **💡 Cobertura essencial, especialmente para profissões de risco!**
            """,
            "destaque": "Proteção contra morte por acidentes"
        },
        {
            "pergunta": "O que é cobertura por invalidez permanente total ou parcial?",
            "resposta": """
            **Cobertura por Invalidez:**
            
            • **Invalidez Total**: Incapacidade para trabalho
            • **Invalidez Parcial**: Perda parcial de capacidade
            • **Por Acidente**: Geralmente sem carência
            • **Por Doença**: Carência de 30-90 dias
            
            **💡 Protege sua renda em caso de incapacidade para trabalhar!**
            
            **Importante**: Define percentuais de acordo com o grau de invalidez.
            """,
            "destaque": "Proteção contra incapacidade para trabalho"
        }
    ],
    "🧑‍💼 4. Beneficiários (101 – 130)": [
        {
            "pergunta": "Quem pode ser beneficiário?",
            "resposta": """
            **Quem Pode Ser Beneficiário:**
            
            • **Qualquer pessoa física** (parentes ou não)
            • **Instituições** (ONGs, fundações)
            • **Herdeiros legais** (se não indicar beneficiários)
            • **Menores de idade** (com representante)
            
            **💡 Você tem liberdade para escolher quem receberá a indenização!**
            
            **Dica**: Sempre indique beneficiários específicos para evitar inventário.
            """,
            "destaque": "Qualquer pessoa física ou instituição"
        },
        {
            "pergunta": "Posso indicar qualquer pessoa?",
            "resposta": """
            **Sim, pode indicar qualquer pessoa:**
            
            • **Cônjuge/Companheiro**
            • **Filhos** (mesmo adotivos)
            • **Pais e avós**
            • **Amigos**
            • **Funcionários**
            • **Instituições de caridade**
            
            **💡 Não é necessário ter parentesco com o beneficiário!**
            
            **Importante**: Para evitar problemas, sempre informe os beneficiários.
            """,
            "destaque": "Sim, qualquer pessoa sem necessidade de parentesco"
        },
        {
            "pergunta": "Posso indicar menores de idade?",
            "resposta": """
            **Sim, pode indicar menores:**
            
            • **Com representante legal** para receber
            • **Valor fica em conta bloqueada** até maioridade
            • **Administrado** por tutor indicado
            • **Pode receber** rendimentos periodicamente
            
            **💡 Perfeito para garantir educação e sustento dos filhos!**
            
            **Dica**: Indique um administrador responsável.
            """,
            "destaque": "Sim, com representante legal para administração"
        },
        {
            "pergunta": "Como indicar um beneficiário?",
            "resposta": """
            **Como Indicar Beneficiários:**
            
            1. **Na proposta**: Durante a contratação
            2. **Por escrito**: Comunicado à seguradora
            3. **Por percentuais**: Definir partes de cada um
            4. **Com dados completos**: Nome, CPF, parentesco
            
            **💡 Pode alterar quantas vezes quiser, sem custo!**
            
            **Importante**: Mantenha sempre atualizado.
            """,
            "destaque": "Na proposta ou por comunicação à seguradora"
        },
        {
            "pergunta": "Preciso informar CPF do beneficiário?",
            "resposta": """
            **Sim, é necessário informar CPF:**
            
            • **Identificação** precisa do beneficiário
            • **Evita confusões** com nomes iguais
            • **Agiliza** o pagamento da indenização
            • **Obrigatório** para pessoas físicas
            
            **💡 Sem o CPF, pode haver dificuldades no pagamento!**
            
            **Dica**: Tenha os CPFs em mãos na hora da contratação.
            """,
            "destaque": "Sim, é obrigatório para identificação precisa"
        }
    ],
    "📊 5. Custos, Prêmios e Valores (131 – 160)": [
        {
            "pergunta": "Quanto custa um seguro de vida?",
            "resposta": """
            **Custo do Seguro de Vida:**
            
            • **A partir de R$ 20/mês** para coberturas básicas
            • **R$ 50-200/mês** para proteção familiar completa
            • **R$ 300+/mês** para alta renda e coberturas especiais
            
            **💡 O custo depende da idade, saúde, profissão e coberturas escolhidas!**
            
            **Dica**: Quanto mais jovem contratar, mais barato será.
            """,
            "destaque": "A partir de R$ 20/mês, varia conforme perfil"
        },
        {
            "pergunta": "Como é calculado o valor do prêmio?",
            "resposta": """
            **Fatores que Influenciam o Prêmio:**
            
            • **Idade** (quanto mais jovem, mais barato)
            • **Sexo** (mulheres geralmente pagam menos)
            • **Profissão** (risco ocupacional)
            • **Hábitos** (fumo, esportes radicais)
            • **Coberturas** escolhidas
            • **Capital segurado**
            
            **💡 Cada seguradora tem sua própria tabela de risco!**
            """,
            "destaque": "Baseado em idade, saúde, profissão e coberturas"
        },
        {
            "pergunta": "Quais fatores influenciam no preço?",
            "resposta": """
            **Principais Fatores de Preço:**
            
            • **Idade**: Principal fator (tabela por idade)
            • **Sexo**: Mulheres têm expectativa de vida maior
            • **Profissão**: Risco ocupacional
            • **Hábitos**: Fumo, álcool, esportes radicais
            • **Histórico médico**: Doenças preexistentes
            • **Coberturas**: Quantidade e valores
            
            **💡 Seja sincero nas informações para evitar problemas futuros!**
            """,
            "destaque": "Idade, sexo, profissão, hábitos e histórico médico"
        },
        {
            "pergunta": "Idade influencia no preço?",
            "resposta": """
            **Sim, a idade é o principal fator:**
            
            • **18-30 anos**: Melhores preços
            • **31-45 anos**: Preços moderados
            • **46-60 anos**: Preços mais altos
            • **61+ anos**: Preços significativamente mais altos
            
            **💡 Contrate jovem para travar preços baixos por mais tempo!**
            
            **Dica**: Alguns seguros têm preço fixo por período.
            """,
            "destaque": "Sim, é o principal fator de precificação"
        },
        {
            "pergunta": "Doenças preexistentes influenciam no preço?",
            "resposta": """
            **Sim, doenças preexistentes influenciam:**
            
            • **Pode aumentar** o prêmio
            • **Pode excluir** cobertura para aquela doença
            • **Pode ter carência** maior
            • **Pode recusar** a proposta em casos graves
            
            **💡 Seja sempre transparente sobre condições médicas!**
            
            **Importante**: Omitir informações pode anular a apólice.
            """,
            "destaque": "Sim, podem aumentar preço ou excluir coberturas"
        }
    ],
    "🧾 6. Contratação e Documentação (161 – 185)": [
        {
            "pergunta": "Como contratar um seguro de vida?",
            "resposta": """
            **Passos para Contratar:**
            
            1. **Análise de necessidades** (quanto e por quanto tempo)
            2. **Cotação** com várias seguradoras
            3. **Preenchimento** da proposta
            4. **Pagamento** do primeiro prêmio
            5. **Análise** pela seguradora
            6. **Emissão** da apólice
            
            **💡 Pode contratar online, por telefone ou com corretor!**
            """,
            "destaque": "Análise, cotação, proposta, pagamento e emissão"
        },
        {
            "pergunta": "Posso contratar online?",
            "resposta": """
            **Sim, pode contratar online:**
            
            • **Site das seguradoras**
            • **Corretoras online**
            • **Comparadores de seguro**
            • **Totalmente digital**
            
            **💡 Processo rápido, seguro e conveniente!**
            
            **Vantagens**: Rapidez, praticidade e often melhores preços.
            """,
            "destaque": "Sim, processo 100% digital disponível"
        },
        {
            "pergunta": "Posso contratar pelo celular?",
            "resposta": """
            **Sim, pode contratar pelo celular:**
            
            • **Apps** das seguradoras
            • **Sites mobile**
            • **WhatsApp** de corretores
            • **Assinatura eletrônica**
            
            **💡 Contrate onde e quando quiser!**
            
            **Conveniência**: Documentação digital e pagamento por PIX/cartão.
            """,
            "destaque": "Sim, através de apps e sites mobile"
        },
        {
            "pergunta": "Preciso apresentar exames?",
            "resposta": """
            **Depende do caso:**
            
            • **Seguros simples**: Geralmente não
            • **Capital alto**: Pode exigir exames
            • **Idade avançada**: Maior probabilidade
            • **Histórico médico**: Pode exigir complementares
            
            **💡 A necessidade de exames varia por seguradora e capital!**
            
            **Dica**: Seguros até R$ 100.000 geralmente não exigem exames.
            """,
            "destaque": "Depende do capital, idade e histórico médico"
        },
        {
            "pergunta": "Quais documentos são exigidos?",
            "resposta": """
            **Documentos Básicos:**
            
            • **CPF** do segurado e beneficiários
            • **RG** ou CNH
            • **Comprovante de residência**
            • **Comprovante de renda** (para capitais altos)
            
            **💡 Documentação simples e rápida!**
            
            **Processo**: Geralmente digital, sem necessidade de cópias físicas.
            """,
            "destaque": "CPF, RG, comprovante de residência e renda"
        }
    ],
    "⚖️ 7. Sinistro e Indenização (186 – 200)": [
        {
            "pergunta": "O que é sinistro?",
            "resposta": """
            **Sinistro é o evento coberto:**
            
            • **Morte** do segurado
            • **Invalidez** permanente
            • **Diagnóstico** de doença grave
            • **Internação** hospitalar
            • **Incapacidade** temporária
            
            **💡 É a ocorrência que dá direito ao recebimento da indenização!**
            
            **Importante**: Comunique o sinistro o mais rápido possível.
            """,
            "destaque": "Evento coberto que gera direito à indenização"
        },
        {
            "pergunta": "Como acionar o seguro?",
            "resposta": """
            **Como Acionar o Seguro:**
            
            1. **Contate a seguradora** imediatamente
            2. **Preencha** formulário de sinistro
            3. **Envie documentos** necessários
            4. **Aguarde análise** (geralmente 30 dias)
            5. **Receba** a indenização
            
            **💡 Pode acionar por telefone, app ou site!**
            
            **Dica**: Tenha a apólice em mãos para agilizar.
            """,
            "destaque": "Contatar seguradora e enviar documentação"
        },
        {
            "pergunta": "Quais documentos são necessários para acionar?",
            "resposta": """
            **Documentos para Sinistro:**
            
            • **Apólice** ou número do contrato
            • **Documentos pessoais** do segurado e beneficiários
            • **Comprovante** do sinistro (atestado óbito, laudo médico)
            • **Formulário** de sinistro preenchido
            
            **💡 Cada tipo de sinistro exige documentos específicos!**
            
            **Dica**: A seguradora informará a lista completa.
            """,
            "destaque": "Apólice, documentos pessoais e comprovante do sinistro"
        },
        {
            "pergunta": "Quem pode solicitar a indenização?",
            "resposta": """
            **Quem Pode Solicitar:**
            
            • **Beneficiários** indicados na apólice
            • **Herdeiros legais** (se não há beneficiários)
            • **Representante legal** (para menores)
            • **Procurador** com poderes específicos
            
            **💡 Os beneficiários não precisam ser parentes!**
            
            **Importante**: Mantenha os beneficiários sempre atualizados.
            """,
            "destaque": "Beneficiários indicados ou herdeiros legais"
        },
        {
            "pergunta": "Quanto tempo leva para pagar a indenização?",
            "resposta": """
            **Prazo para Pagamento:**
            
            • **30 dias** após documentação completa
            • **Casos simples**: 15-20 dias
            • **Casos complexos**: Até 45 dias
            • **Com documentação incompleta**: Pode demorar mais
            
            **💡 A agilidade depende da qualidade da documentação!**
            
            **Dica**: Envie todos os documentos de uma vez para agilizar.
            """,
            "destaque": "Até 30 dias após documentação completa"
        }
    ]
}

# ---------- INTERFACE PRINCIPAL ----------
st.markdown("""
<div class="main-header floating-card">
    <h1 class="main-title">🚀 BeSmart PRO</h1>
    <h3 style="font-size: 1.8rem; margin-bottom: 1rem; opacity: 0.9; font-weight: 300;">Sistema Inteligente de Cálculo de Capital Segurado</h3>
    <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin-top: 2rem;">
        <span style="background: rgba(255,255,255,0.2); padding: 0.8rem 1.8rem; border-radius: 25px; backdrop-filter: blur(10px); font-weight: 500;">🌟 Omint</span>
        <span style="background: rgba(255,255,255,0.2); padding: 0.8rem 1.8rem; border-radius: 25px; backdrop-filter: blur(10px); font-weight: 500;">💫 MAG</span>
        <span style="background: rgba(255,255,255,0.2); padding: 0.8rem 1.8rem; border-radius: 25px; backdrop-filter: blur(10px); font-weight: 500;">⚡ Icatu</span>
        <span style="background: rgba(255,255,255,0.2); padding: 0.8rem 1.8rem; border-radius: 25px; backdrop-filter: blur(10px); font-weight: 500;">🔮 Prudential</span>
        <span style="background: rgba(255,255,255,0.2); padding: 0.8rem 1.8rem; border-radius: 25px; backdrop-filter: blur(10px); font-weight: 500;">🎯 MetLife</span>
        <span style="background: rgba(255,255,255,0.2); padding: 0.8rem 1.8rem; border-radius: 25px; backdrop-filter: blur(10px); font-weight: 500;">🚀 Azos</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Navegação
st.sidebar.markdown("""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 15px; text-align: center; margin-bottom: 2rem; box-shadow: 0 6px 20px rgba(0,0,0,0.15);">
    <h3 style="color: white; margin: 0; font-size: 1.5rem;">🧭 Navegação</h3>
</div>
""", unsafe_allow_html=True)

aba_selecionada = st.sidebar.radio("", [
    "🎯 Dashboard", 
    "👤 Cadastro Completo", 
    "🏆 Seguradoras Recomendadas",
    "🛡️ Análise de Coberturas",
    "❓ FAQ Interativo"  
], label_visibility="collapsed")

# ---------- ABA 1: DASHBOARD ----------
if aba_selecionada == "🎯 Dashboard":
    st.markdown('<div class="section-title">📊 Dashboard Interativo</div>', unsafe_allow_html=True)
    
    if st.session_state.cliente:
        cliente = st.session_state.cliente
        risk_score = InsuranceAI.calculate_risk_score(cliente)
        calculo = CalculadoraCapital.calcular_capital_total(cliente)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size: 1rem; color: #666; margin-bottom: 0.8rem;">💰 Capital Sugerido</div>
                <div style="font-size: 2rem; font-weight: bold; color: #667eea; margin-bottom: 0.5rem;">{formatar_moeda(calculo['capital_total'])}</div>
                <div style="font-size: 0.9rem; color: #28a745; background: rgba(40, 167, 69, 0.1); padding: 0.3rem 0.8rem; border-radius: 10px; display: inline-block;">↑ Recomendação Ideal</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            risco_cor = '#dc3545' if risk_score < 50 else '#ffc107' if risk_score < 70 else '#28a745'
            risco_texto = '🔴 Alto Risco' if risk_score < 50 else '🟡 Médio Risco' if risk_score < 70 else '🟢 Baixo Risco'
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size: 1rem; color: #666; margin-bottom: 0.8rem;">🛡️ Score de Risco</div>
                <div style="font-size: 2rem; font-weight: bold; color: {risco_cor}; margin-bottom: 0.5rem;">{risk_score}/100</div>
                <div style="font-size: 0.9rem; color: {risco_cor}; background: rgba(220, 53, 69, 0.1); padding: 0.3rem 0.8rem; border-radius: 10px; display: inline-block;">{risco_texto}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size: 1rem; color: #666; margin-bottom: 0.8rem;">👨‍👩‍👧‍👦 Dependentes</div>
                <div style="font-size: 2rem; font-weight: bold; color: #17a2b8; margin-bottom: 0.5rem;">{cliente.get('dependentes', 0)}</div>
                <div style="font-size: 0.9rem; color: #17a2b8; background: rgba(23, 162, 184, 0.1); padding: 0.3rem 0.8rem; border-radius: 10px; display: inline-block;">Pessoas protegidas</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            coberturas_ativas = len([v for v in calculo['coberturas_detalhadas'].values() if v > 0])
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size: 1rem; color: #666; margin-bottom: 0.8rem;">📊 Coberturas</div>
                <div style="font-size: 2rem; font-weight: bold; color: #6f42c1; margin-bottom: 0.5rem;">{coberturas_ativas}</div>
                <div style="font-size: 0.9rem; color: #6f42c1; background: rgba(111, 66, 193, 0.1); padding: 0.3rem 0.8rem; border-radius: 10px; display: inline-block;">Proteções ativas</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Capital Total
        st.markdown(f"""
        <div class="capital-total">
            <h3 class="capital-title">💎 CAPITAL TOTAL SUGERIDO</h3>
            <p class="capital-value">{formatar_moeda(calculo['capital_total'])}</p>
            <p class="capital-subtitle">Proteção completa e personalizada para você e sua família</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Análise de Riscos
        show_risk_analysis(cliente)
        
        # Storytelling Personalizado
        st.markdown('<div class="subsection-title">📖 Sua Jornada de Proteção</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="success-card">
            {InsuranceAI.generate_personalized_story(cliente)}
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.markdown("""
        <div style="text-align: center; padding: 4rem 2rem; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); margin: 2rem 0;">
            <h2 style="color: #667eea; margin-bottom: 1.5rem; font-size: 2.5rem;">👋 Bem-vindo ao BeSmart PRO!</h2>
            <p style="font-size: 1.3rem; color: #666; margin-bottom: 2rem; line-height: 1.6;">Complete seu cadastro para descobrir o <span class="highlight-text">capital segurado ideal</span> para sua proteção.</p>
            <div style="font-size: 5rem; margin-bottom: 2rem;">🚀</div>
            <p style="color: #999; font-size: 1.1rem;">Sistema Inteligente de Cálculo de Capital Segurado</p>
        </div>
        """, unsafe_allow_html=True)

# ---------- ABA 2: CADASTRO COMPLETO ----------
elif aba_selecionada == "👤 Cadastro Completo":
    st.markdown('<div class="section-title">👤 Cadastro Completo para Cálculo de Capital</div>', unsafe_allow_html=True)
    
    create_progress_tracker(1)
    
    with st.form("cadastro_completo"):
        st.markdown("""
        <div class="section-header">
            <h3 style="margin: 0; font-size: 1.5rem;">📋 Informações Básicas</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="info-card">
                <h4 style="margin: 0 0 1rem 0; color: #2c3e50;">📝 Dados Pessoais</h4>
            """, unsafe_allow_html=True)
            nome = st.text_input("**Nome Completo***", placeholder="Digite seu nome completo", help="Nome completo do cliente")
            idade = st.number_input("**Idade***", min_value=18, max_value=80, value=30, help="Idade entre 18 e 80 anos")
            profissao = st.text_input("**Profissão***", placeholder="Sua profissão atual", help="Profissão principal do cliente")
            dependentes = st.number_input("**Número de dependentes***", min_value=0, max_value=10, value=0, help="Pessoas que dependem financeiramente do cliente")
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="info-card">
                <h4 style="margin: 0 0 1rem 0; color: #2c3e50;">💰 Situação Financeira</h4>
            """, unsafe_allow_html=True)
            renda_mensal = st.number_input("**Renda Mensal Líquida (R$)***", min_value=0.0, value=5000.0, step=500.0, format="%.2f", help="Renda líquida mensal do cliente")
            patrimonio_total = st.number_input("**Patrimônio Total (R$)**", min_value=0.0, value=0.0, step=10000.0, format="%.2f",
                                             help="Patrimônio total incluindo imóveis, investimentos, veículos, etc.")
            despesas_mensais = st.number_input("**Despesas Mensais Fixas (R$)***", min_value=0.0, value=2000.0, step=100.0, format="%.2f", help="Despesas mensais fixas do cliente")
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="section-header">
            <h3 style="margin: 0; font-size: 1.5rem;">👨‍👩‍👧‍👦 Dados Familiares</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.markdown("""
            <div class="info-card">
                <h4 style="margin: 0 0 1rem 0; color: #2c3e50;">🏠 Despesas Familiares</h4>
            """, unsafe_allow_html=True)
            despesas_filhos_mensais = st.number_input("**Despesas Mensais com Filhos (R$)**", min_value=0.0, value=0.0, step=100.0, format="%.2f",
                                                    help="Despesas com educação, saúde, alimentação dos filhos")
            anos_ate_independencia = st.number_input("**Anos até Independência dos Filhos**", min_value=0, max_value=30, value=0,
                                                   help="Anos até que os filhos se tornem independentes financeiramente")
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="info-card">
                <h4 style="margin: 0 0 1rem 0; color: #2c3e50;">💡 Informações Importantes</h4>
                <p style="color: #666; line-height: 1.5; margin: 0;">
                    <strong>DIT e DIH:</strong> Calculados automaticamente como <strong>(Despesas Mensais) / 30</strong><br><br>
                    Estes valores representam o valor diário necessário para manter seu padrão de vida durante incapacidade ou internação.
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="section-header">
            <h3 style="margin: 0; font-size: 1.5rem;">🎯 Perfil do Cliente</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <p style="color: #666; margin-bottom: 1rem; font-size: 1rem;">
                Selecione os perfis que melhor se aplicam ao cliente. Esta informação nos ajudará a recomendar as <strong>melhores seguradoras</strong> para suas necessidades específicas.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col5, col6 = st.columns(2)
        perfil_cliente = {}
        
        with col5:
            for i, perfil in enumerate(PERFIS_CLIENTE[:10]):
                perfil_cliente[perfil] = st.checkbox(f"**{perfil}**", key=f"perfil_{i}")
        
        with col6:
            for i, perfil in enumerate(PERFIS_CLIENTE[10:]):
                perfil_cliente[perfil] = st.checkbox(f"**{perfil}**", key=f"perfil_{i+10}")
        
        st.markdown("""
        <div class="section-header">
            <h3 style="margin: 0; font-size: 1.5rem;">👔 Dados do Assessor</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col7, col8 = st.columns(2)
        
        with col7:
            st.markdown("""
            <div class="info-card">
                <h4 style="margin: 0 0 1rem 0; color: #2c3e50;">🏢 Filial</h4>
            """, unsafe_allow_html=True)
            filial = st.selectbox("**Filial***", FILIAIS, help="Selecione a filial do assessor")
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col8:
            st.markdown("""
            <div class="info-card">
                <h4 style="margin: 0 0 1rem 0; color: #2c3e50;">👤 Assessor</h4>
            """, unsafe_allow_html=True)
            assessor = st.text_input("**Nome do Assessor***", placeholder="Nome do seu assessor BeSmart", help="Nome do assessor responsável")
            st.markdown("</div>", unsafe_allow_html=True)
        
        submitted = st.form_submit_button("🚀 **Calcular Capital Segurado**", use_container_width=True)
        
        if submitted:
            if nome and profissao and renda_mensal > 0 and despesas_mensais > 0 and filial and assessor:
                calculo = CalculadoraCapital.calcular_capital_total({
                    'nome': nome,
                    'idade': idade,
                    'profissao': profissao,
                    'dependentes': dependentes,
                    'renda_mensal': renda_mensal,
                    'patrimonio_total': patrimonio_total,
                    'despesas_mensais': despesas_mensais,
                    'despesas_filhos_mensais': despesas_filhos_mensais,
                    'anos_ate_independencia': anos_ate_independencia
                })
                
                st.session_state.cliente = {
                    'nome': nome,
                    'idade': idade,
                    'profissao': profissao,
                    'dependentes': dependentes,
                    'renda_mensal': renda_mensal,
                    'patrimonio_total': patrimonio_total,
                    'despesas_mensais': despesas_mensais,
                    'despesas_filhos_mensais': despesas_filhos_mensais,
                    'anos_ate_independencia': anos_ate_independencia,
                    'filial': filial,
                    'assessor': assessor,
                    'capital_sugerido': calculo['capital_total'],
                    'detalhes_calculo': calculo['coberturas_detalhadas']
                }
                
                st.session_state.perfil_cliente = perfil_cliente
                st.session_state.simulation_step = 2
                st.session_state.calculation_complete = True
                
                st.success("""
                **✅ Capital segurado calculado com sucesso!**
                
                Seu capital segurado ideal foi calculado com base nas informações fornecidas e na metodologia da tabela BeSmart.
                """)
                st.balloons()
                
                st.markdown('<div class="subsection-title">📊 Resumo do Cálculo</div>', unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div style="font-size: 1rem; color: #666;">Capital Total Sugerido</div>
                        <div style="font-size: 2rem; font-weight: bold; color: #667eea;">{formatar_moeda(calculo['capital_total'])}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.info(f"**👤 Idade:** {idade} anos")
                    st.info(f"**👨‍👩‍👧‍👦 Dependentes:** {dependentes}")
                
                with col2:
                    st.info(f"**💰 Renda Mensal:** {formatar_moeda(renda_mensal)}")
                    st.info(f"**🏠 Patrimônio:** {formatar_moeda(patrimonio_total)}")
                    st.info(f"**💸 Despesas Mensais:** {formatar_moeda(despesas_mensais)}")
                
                with st.expander("📈 **Detalhamento das Coberturas**", expanded=True):
                    for cobertura, valor in calculo['coberturas_detalhadas'].items():
                        if valor > 0:
                            if 'Diária' in cobertura:
                                st.write(f"**🛡️ {cobertura}:** {formatar_moeda(valor)}/dia")
                            else:
                                st.write(f"**🛡️ {cobertura}:** {formatar_moeda(valor)}")
                
                st.markdown('<div class="subsection-title">🏆 Melhores Seguradoras para seu Perfil</div>', unsafe_allow_html=True)
                melhores_seguradoras = SistemaRecomendacao.recomendar_melhores_seguradoras(perfil_cliente)
                
                for melhor in melhores_seguradoras:
                    emoji = {1: "🥇", 2: "🥈", 3: "🥉"}[melhor['posicao']]
                    st.success(f"{emoji} **{melhor['seguradora']}** - **{melhor['score']} pontos** ({melhor['porcentagem']:.1f}% compatibilidade)")
                
                st.success(f"**👔 Seu assessor {assessor} da filial {filial} entrará em contato em breve!**")
                
            else:
                st.error("""
                **⚠️ Por favor, preencha todos os campos obrigatórios (*)**
                
                Certifique-se de que:
                - Nome completo está preenchido
                - Profissão está informada
                - Renda mensal é maior que zero
                - Despesas mensais são maiores que zero
                - Filial foi selecionada
                - Nome do assessor está preenchido
                """)

# ---------- ABA 3: SEGURADORAS RECOMENDADAS ----------
elif aba_selecionada == "🏆 Seguradoras Recomendadas":
    st.markdown('<div class="section-title">🏆 Seguradoras Recomendadas</div>', unsafe_allow_html=True)
    
    if not st.session_state.cliente:
        st.warning("""
        **⚠️ Complete seu cadastro primeiro para ver recomendações personalizadas!**
        
        Acesse a aba **👤 Cadastro Completo** para fornecer suas informações e receber recomendações específicas para seu perfil.
        """)
        st.stop()
    
    cliente = st.session_state.cliente
    perfil_cliente = st.session_state.perfil_cliente
    create_progress_tracker(3)
    
    recommendations = InsuranceAI.recommend_insurers(cliente, perfil_cliente)
    melhores_seguradoras = SistemaRecomendacao.recomendar_melhores_seguradoras(perfil_cliente)
    
    st.markdown('<div class="subsection-title">🎯 Seguradoras Compatíveis com Seu Perfil</div>', unsafe_allow_html=True)
    st.write(f"**Baseado no seu perfil:** **{cliente['profissao']}**, **{cliente['idade']} anos**, **Renda {formatar_moeda(cliente['renda_mensal'])}**")
    
    # Mostrar top 3 melhores seguradoras
    st.markdown('<div class="subsection-title">🥇 Melhores Seguradoras para seu Perfil</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    posicoes = {1: col1, 2: col2, 3: col3}
    
    for melhor in melhores_seguradoras:
        with posicoes[melhor['posicao']]:
            emoji = {1: "🥇", 2: "🥈", 3: "🥉"}[melhor['posicao']]
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 2rem; border-radius: 20px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.2); margin-bottom: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">{emoji}</div>
                <h3 style="margin: 0 0 1rem 0; font-size: 1.8rem;">{melhor['seguradora']}</h3>
                <p style="margin: 0.5rem 0; font-size: 1.2rem;"><strong>Pontuação:</strong> {melhor['score']} pts</p>
                <p style="margin: 0.5rem 0; font-size: 1.2rem;"><strong>Compatibilidade:</strong> {melhor['porcentagem']:.1f}%</p>
            </div>
            """, unsafe_allow_html=True)
            
            with st.expander(f"📋 **Ver detalhes de {melhor['seguradora']}**"):
                st.write("**🎯 Perfis que mais contribuíram:**")
                for perfil, peso in list(melhor['detalhes'].items())[:5]:
                    if peso > 5:
                        especificidade = "🔴 Alta" if peso >= 80 else "🟡 Média" if peso >= 50 else "🟢 Baixa"
                        st.write(f"- **{perfil}:** {peso} pontos ({especificidade})")
    
    # Seção de downloads
    st.markdown("---")
    st.markdown('<div class="subsection-title">📥 Download da Proposta</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        proposta_txt = gerar_proposta_txt(cliente, recommendations, melhores_seguradoras)
        download_txt = criar_download_button(
            proposta_txt, 
            f"proposta_besmart_{cliente.get('nome', 'cliente')}.txt", 
            "📄 Baixar Proposta Completa (TXT)", 
            'txt'
        )
        st.markdown(download_txt, unsafe_allow_html=True)
    
    with col2:
        dados_csv = {
            'Cliente': [cliente.get('nome', '')],
            'Capital_Sugerido': [cliente.get('capital_sugerido', 0)],
            'Renda_Mensal': [cliente.get('renda_mensal', 0)],
            'Patrimonio': [cliente.get('patrimonio_total', 0)],
            'Dependentes': [cliente.get('dependentes', 0)],
            'Melhor_Seguradora': [melhores_seguradoras[0]['seguradora'] if melhores_seguradoras else ''],
            'Pontuacao_Melhor': [melhores_seguradoras[0]['score'] if melhores_seguradoras else 0],
            'Compatibilidade_Melhor': [melhores_seguradoras[0]['porcentagem'] if melhores_seguradoras else 0]
        }
        df_csv = pd.DataFrame(dados_csv)
        
        download_csv = criar_download_button(
            df_csv,
            f"dados_cliente_{cliente.get('nome', 'cliente')}.csv",
            "📊 Baixar Dados Resumidos (CSV)",
            'csv'
        )
        st.markdown(download_csv, unsafe_allow_html=True)

# ---------- ABA 4: ANÁLISE DE COBERTURAS ----------
elif aba_selecionada == "🛡️ Análise de Coberturas":
    st.markdown('<div class="section-title">🛡️ Análise de Coberturas</div>', unsafe_allow_html=True)
    
    if not st.session_state.cliente:
        st.warning("""
        **⚠️ Complete seu cadastro primeiro para uma análise personalizada!**
        
        Acesse a aba **👤 Cadastro Completo** para fornecer suas informações e receber uma análise detalhada das coberturas ideais para você.
        """)
        
        # Preview das coberturas disponíveis
        st.markdown("""
        <div class="info-card">
            <h4 style="color: #2c3e50; margin-bottom: 1rem;">💫 Conheça Nossas Coberturas</h4>
            <p style="color: #666; line-height: 1.6;">
                Oferecemos <strong>6 tipos de coberturas</strong> personalizadas para suas necessidades:
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Grid de coberturas em preview
        col1, col2 = st.columns(2)
        
        with col1:
            for nome, dados in list(COBERTURAS_DETALHADAS.items())[:3]:
                st.markdown(f"""
                <div class="coverage-type-card" style="border-color: {dados['cor']}">
                    <div class="coverage-icon">{dados['icone']}</div>
                    <h4 style="color: #2c3e50; margin-bottom: 0.5rem;">{nome}</h4>
                    <p style="color: #666; font-size: 0.9rem; line-height: 1.4;">{dados['descricao'][:100]}...</p>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            for nome, dados in list(COBERTURAS_DETALHADAS.items())[3:]:
                st.markdown(f"""
                <div class="coverage-type-card" style="border-color: {dados['cor']}">
                    <div class="coverage-icon">{dados['icone']}</div>
                    <h4 style="color: #2c3e50; margin-bottom: 0.5rem;">{nome}</h4>
                    <p style="color: #666; font-size: 0.9rem; line-height: 1.4;">{dados['descricao'][:100]}...</p>
                </div>
                """, unsafe_allow_html=True)
        
        st.info("""
        **💡 Complete seu cadastro para receber:**
        - Análise personalizada das coberturas
        - Cálculo automático dos valores ideais
        - Recomendações específicas para seu perfil
        - Comparação entre seguradoras
        """)
        
    else:
        cliente = st.session_state.cliente
        calculo = CalculadoraCapital.calcular_capital_total(cliente)
        
        # Hero Section
        create_coverage_hero(cliente, calculo)
        
        # Seção principal de coberturas - MODIFICADA
        st.markdown('<div class="subsection-title">🎯 Suas Coberturas Calculadas</div>', unsafe_allow_html=True)
        
        # Grid de coberturas simplificado - APENAS NOME E BOTÃO VER DETALHES
        cols = st.columns(3)
        coberturas = calculo['coberturas_detalhadas']
        
        for i, (cobertura_nome, valor) in enumerate(coberturas.items()):
            with cols[i % 3]:
                dados_cobertura = COBERTURAS_DETALHADAS[cobertura_nome]
                
                # Determinar se a cobertura é relevante
                is_relevante = valor > 0
                badge_text = "✅ Ativa" if is_relevante else "💡 Recomendada"
                badge_cor = "#28a745" if is_relevante else "#6c757d"
                
                st.markdown(f"""
                <div class="coverage-type-card" style="border-color: {dados_cobertura['cor']}">
                    <div class="coverage-badge" style="background: {badge_cor}">{badge_text}</div>
                    <div class="coverage-icon">{dados_cobertura['icone']}</div>
                    <h3 class="coverage-name">{cobertura_nome}</h3>
                    <div class="coverage-value">
                        {formatar_moeda(valor) if 'Diária' not in cobertura_nome else formatar_moeda(valor) + '/dia'}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Botão para expandir detalhes
                if st.button(f"📊 Ver Detalhes", key=f"btn_{cobertura_nome}", use_container_width=True):
                    st.session_state.selected_coverage = cobertura_nome
                    st.session_state.coverage_details_expanded[cobertura_nome] = True
        
        # Mostrar card detalhado se alguma cobertura foi selecionada
        if st.session_state.selected_coverage:
            cobertura_selecionada = st.session_state.selected_coverage
            dados_selecionados = COBERTURAS_DETALHADAS[cobertura_selecionada]
            valor_selecionado = coberturas[cobertura_selecionada]
            
            if st.session_state.coverage_details_expanded.get(cobertura_selecionada, False):
                st.markdown("---")
                show_detailed_coverage_card(cobertura_selecionada, dados_selecionados, valor_selecionado, cliente)
        
        # Gráfico abaixo totalmente lindo e perfeito, bem enquadrado e estruturado
        st.markdown("---")
        st.markdown("""
        <div class="chart-container">
            <h3 style="color: #2c3e50; margin-bottom: 2rem; text-align: center;">📊 Distribuição do Capital por Cobertura</h3>
        """, unsafe_allow_html=True)
        
        # Gráfico de distribuição
        create_coverage_comparison_chart(calculo)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Análise Visual
        st.markdown("---")
        st.markdown('<div class="subsection-title">🎯 Níveis de Proteção da Sua Carteira</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Níveis de proteção
            create_protection_level_analysis(cliente, calculo)
        
        with col2:
            # Métricas Resumo
            st.markdown('<div class="subsection-title">📈 Métricas da Sua Carteira</div>', unsafe_allow_html=True)
            
            coberturas_ativas = len([v for v in coberturas.values() if v > 0])
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size: 1rem; color: #666; margin-bottom: 0.8rem;">🛡️ Coberturas Ativas</div>
                <div style="font-size: 2rem; font-weight: bold; color: #667eea; margin-bottom: 0.5rem;">{coberturas_ativas}/6</div>
                <div style="font-size: 0.9rem; color: #28a745; background: rgba(40, 167, 69, 0.1); padding: 0.3rem 0.8rem; border-radius: 10px; display: inline-block;">
                    {f"{coberturas_ativas/6*100:.0f}% do potencial" if coberturas_ativas > 0 else "Complete seu perfil"}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            maior_cobertura = max(coberturas.values()) if coberturas_ativas > 0 else 0
            nome_maior = [k for k, v in coberturas.items() if v == maior_cobertura][0] if coberturas_ativas > 0 else "Nenhuma"
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size: 1rem; color: #666; margin-bottom: 0.8rem;">💰 Maior Cobertura</div>
                <div style="font-size: 1.5rem; font-weight: bold; color: #28a745; margin-bottom: 0.5rem;">{formatar_moeda(maior_cobertura)}</div>
                <div style="font-size: 0.9rem; color: #666;">{nome_maior}</div>
            </div>
            """, unsafe_allow_html=True)
            
            protecao_renda = sum([coberturas['Invalidez Permanente'], coberturas['Diária Incapacidade Temporária'] * 30 * 6])
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size: 1rem; color: #666; margin-bottom: 0.8rem;">💼 Proteção de Renda</div>
                <div style="font-size: 1.5rem; font-weight: bold; color: #ffc107; margin-bottom: 0.5rem;">{formatar_moeda(protecao_renda)}</div>
                <div style="font-size: 0.9rem; color: #666;">+6 meses de sustento</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Recomendações Inteligentes
        st.markdown("---")
        create_coverage_recommendations(cliente, calculo)

# ---------- ABA 5: FAQ INTERATIVO ----------
elif aba_selecionada == "❓ FAQ Interativo":
    st.markdown('<div class="section-title">❓ FAQ Interativo</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="success-card">
        <h2 style="margin: 0 0 1rem 0; font-size: 2.5rem; text-align: center;">💫 Centro de Ajuda BeSmart</h2>
        <p style="font-size: 1.3rem; opacity: 0.9; text-align: center; margin: 0;">Encontre respostas claras para todas suas dúvidas sobre seguros</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Barra de pesquisa
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        pesquisa = st.text_input("**🔍 Pesquisar no FAQ:**", placeholder="Digite sua dúvida...", help="Encontre respostas específicas")
    
    with col2:
        categoria_selecionada = st.selectbox("**📂 Filtrar por categoria:**", [
            "Todas as Categorias",
            "🧭 1. Conceitos Gerais e Funcionamento (1 – 30)",
            "📝 2. Tipos e Modalidades de Seguro (31 – 60)", 
            "💰 3. Coberturas e Benefícios (61 – 100)",
            "🧑‍💼 4. Beneficiários (101 – 130)",
            "📊 5. Custos, Prêmios e Valores (131 – 160)",
            "🧾 6. Contratação e Documentação (161 – 185)",
            "⚖️ 7. Sinistro e Indenização (186 – 200)"
        ])
    
    # Função para criar FAQ interativo
    def create_faq_section():
        categorias_exibidas = []
        
        if categoria_selecionada == "Todas as Categorias":
            categorias_exibidas = list(FAQ_COMPLETO.keys())
        else:
            categorias_exibidas = [categoria_selecionada]
        
        for categoria in categorias_exibidas:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #00b09b 0%, #96c93d 100%); color: white; padding: 1rem 2rem; border-radius: 15px; margin: 2rem 0 1rem 0;">
                <h3 style="margin: 0; font-size: 1.5rem;">{categoria}</h3>
            </div>
            """, unsafe_allow_html=True)
            
            perguntas_filtradas = FAQ_COMPLETO[categoria]
            
            if pesquisa:
                perguntas_filtradas = [
                    p for p in perguntas_filtradas 
                    if pesquisa.lower() in p['pergunta'].lower() or 
                       pesquisa.lower() in p['resposta'].lower() or
                       pesquisa.lower() in p['destaque'].lower()
                ]
            
            if not perguntas_filtradas:
                st.info("🔍 Nenhuma pergunta encontrada com os filtros atuais.")
            else:
                for i, pergunta_data in enumerate(perguntas_filtradas):
                    with st.expander(f"**{pergunta_data['pergunta']}**", expanded=False):
                        st.markdown(f"""
                        <div class="info-card">
                            <div style="color: #666; line-height: 1.6; margin-bottom: 1rem;">
                                {pergunta_data['resposta']}
                            
                        """, unsafe_allow_html=True)
    
    create_faq_section()
    
    # Seção de ajuda adicional
    st.markdown("---")
    st.markdown('<div class="subsection-title">💬 Não encontrou sua dúvida?</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
       
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #00b09b 0%, #96c93d 100%); color: white; border-radius: 15px;">
            <div style="font-size: 2rem;">💬</div>
            <h4>WhatsApp</h4>
            <p>(21) 99799-4515</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; border-radius: 15px;">
            <div style="font-size: 2rem;">📧</div>
            <h4>E-mail</h4>
            <p>vida@besmart.com.br</p>
        </div>
        """, unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("---")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%); padding: 1.5rem; border-radius: 15px; color: white; margin-bottom: 1rem; box-shadow: 0 6px 20px rgba(0,0,0,0.15);">
        <h4 style="margin: 0; text-align: center; font-size: 1.3rem;">🏢 Nossas Seguradoras</h4>
    </div>
    """, unsafe_allow_html=True)
    
    seguradoras_html = """
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.8rem; margin-bottom: 1rem;">
        <div style="background: rgba(255,255,255,0.15); padding: 0.8rem; border-radius: 10px; text-align: center; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
            <div style="font-size: 0.9rem; font-weight: 500;">🌟 Omint</div>
        </div>
        <div style="background: rgba(255,255,255,0.15); padding: 0.8rem; border-radius: 10px; text-align: center; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
            <div style="font-size: 0.9rem; font-weight: 500;">💫 MAG</div>
        </div>
        <div style="background: rgba(255,255,255,0.15); padding: 0.8rem; border-radius: 10px; text-align: center; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
            <div style="font-size: 0.9rem; font-weight: 500;">⚡ Icatu</div>
        </div>
        <div style="background: rgba(255,255,255,0.15); padding: 0.8rem; border-radius: 10px; text-align: center; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
            <div style="font-size: 0.9rem; font-weight: 500;">🔮 Prudential</div>
        </div>
        <div style="background: rgba(255,255,255,0.15); padding: 0.8rem; border-radius: 10px; text-align: center; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
            <div style="font-size: 0.9rem; font-weight: 500;">🎯 MetLife</div>
        </div>
        <div style="background: rgba(255,255,255,0.15); padding: 0.8rem; border-radius: 10px; text-align: center; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
            <div style="font-size: 0.9rem; font-weight: 500;">🚀 Azos</div>
        </div>
    </div>
    """
    st.markdown(seguradoras_html, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; border-radius: 15px; color: white; margin-bottom: 1rem; box-shadow: 0 6px 20px rgba(0,0,0,0.15);">
        <h4 style="margin: 0; text-align: center; font-size: 1.3rem;">⚡ Ações Rápidas</h4>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📄 **Relatório**", use_container_width=True):
            if st.session_state.cliente:
                st.success("**📊 Relatório gerado com sucesso!**")
            else:
                st.warning("**Complete o cadastro primeiro!**")
    
    with col2:
        if st.button("🔄 **Nova Simulação**", use_container_width=True):
            st.session_state.cliente = {}
            st.session_state.perfil_cliente = {}
            st.session_state.simulation_step = 0
            st.session_state.calculation_complete = False
            st.rerun()
    
    st.markdown("---")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #00b09b 0%, #96c93d 100%); padding: 2rem; border-radius: 15px; color: white; box-shadow: 0 6px 20px rgba(0,0,0,0.15);">
        <h4 style="margin: 0 0 1.5rem 0; text-align: center; font-size: 1.3rem;">🤝 Vida BeSmart</h4>
        <div style="text-align: center; margin-bottom: 1.5rem;">
            <div style="margin-bottom: 0.8rem; font-size: 1.1rem;">📞 <strong>(21) 99799-4515</strong></div>
            <div style="margin-bottom: 0.8rem; font-size: 1.1rem;">💬 <strong>WhatsApp Chat</strong></div>
            <div style="font-size: 1.1rem;">🎯 <strong>Consultor Dedicado</strong></div>
        </div>
        <div style="margin-top: 1.5rem; font-size: 0.9rem; text-align: center;">
            <div style="margin-bottom: 0.5rem;">🔒 <strong>Dados Criptografados</strong></div>
            <div style="margin-bottom: 0.5rem;">✓ <strong>Conformidade LGPD</strong></div>
            <div>✓ <strong>Certificação Digital</strong></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------- ANIMAÇÕES ----------
if st.session_state.get('cliente'):
    st.balloons()
    
if st.session_state.get('calculation_complete'):
    st.markdown("""
    <script>
    setTimeout(() => {
    }, 1000);
    </script>
    """, unsafe_allow_html=True)
    st.session_state.calculation_complete = False