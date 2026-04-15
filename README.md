# Distributed Brute Force Attack Detection System
venv\Scripts\activate
## Overview
This project implements a log-based cybersecurity detection system designed to identify distributed brute force attacks targeting authentication services.

Unlike traditional detectors that rely on single-IP thresholds, this system analyzes behavioral patterns across multiple IP addresses attacking a single user account.

---

## Problem Statement
Traditional brute force detection fails when attackers distribute login attempts across many IP addresses.

This project detects:
- Single-source brute force attacks
- Distributed brute force attacks
- Low-and-slow credential attacks

---

## System Architecture

Log Sources → Filebeat → Logstash → Elasticsearch → Detection Engine → Alert System → Kibana Dashboard

---

## Core Components
- Log Collection
- Log Preprocessing
- Detection Engine
- Machine Learning Analysis
- Real-time Alerting
- Visualization Dashboard

---

## Technologies
- ELK Stack
- Python
- Scikit-learn
- Kibana