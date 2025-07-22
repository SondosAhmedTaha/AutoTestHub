#!/bin/bash
set -e

echo "🐳 Building Docker image with docker-compose..."
docker-compose build

echo "🚀 Running container and saving report to ./reports..."
docker-compose run --rm autotesthub

echo "📋 Showing last test results from MongoDB:"
docker-compose run --rm autotesthub python src/view_results.py
