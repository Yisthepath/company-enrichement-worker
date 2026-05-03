# Company Enrichment Worker

A Python background data pipeline that enriches company websites into structured company intelligence.

This project is designed as the worker layer for a larger SaaS idea: a company intelligence platform for sales teams. The worker takes raw company inputs, visits public company websites, extracts useful information, cleans and validates the data, saves it to a database, and optionally uses a local open-source LLM to generate company insights.

## Project Overview

Modern sales workflows depend on accurate company data. Sales teams want to find growing companies that may need their product.

This project focuses on the backend worker system that could power those workflows.

The worker is responsible for:

- loading company records
- validating and normalizing company websites
- fetching public website pages
- handling failed requests safely
- extracting company information from HTML
- detecting useful business signals
- validating structured company profiles
- saving data to a database
- tracking worker runs and failures
- processing enrichment jobs in the background
- optionally using a local open-source LLM for summaries and classification

## Problem This Project Solves

Raw company data is often messy.

Examples:

- missing websites
- invalid URLs
- duplicate companies
- broken domains
- websites that return 404, 403, or 500 errors
- pages with missing metadata
- inconsistent company names
- vague or unstructured website text

A reliable company intelligence system needs a worker that can process this messy input without crashing.

This project solves that by building a structured enrichment pipeline.

## Target Users

This project is built for sales teams who could use enriched company data to:

- discover potential leads
- identify companies with hiring or growth signals
- understand what a company does
- find relevant outreach angles
- prioritize accounts

## Core Pipeline

The worker follows this general flow:

```text
Company input
    ↓
Validate company record
    ↓
Normalize website URL
    ↓
Fetch public website HTML
    ↓
Handle request errors
    ↓
Parse HTML
    ↓
Extract title, description, headings, and links
    ↓
Detect careers pages and other pages that display hiring/growth signals
    ↓
Clean extracted data
    ↓
Validate structured company profile
    ↓
Save to database
    ↓
Log success or failure
    ↓
Optional LLM enrichment