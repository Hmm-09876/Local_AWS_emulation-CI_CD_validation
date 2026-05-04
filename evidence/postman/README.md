# Postman Evidence

This folder contains files related to API testing using Postman.

The goal of this folder is to record the process of learning how to use Postman to test basic APIs, and to keep the test results as evidence.

## What’s in this folder

### `api smoke tests.postman_collection.json`
A collection containing the requests created to test the app in the repo.

Basic requests:
- `GET /`
- `GET /health`
- `GET /no-such-route`

### `demo-3.postman_environment.json`
An environment containing variables used when running locally.

Main variable:
- `base_url = http://localhost:8080`

### `run-notes.md`
A file with short notes about each test run:
- Which URL the app was running on
- Which requests were tested
- Pass or fail
- Anything that needs adjustment

## Objective

This Postman setup is only used at the smoke test level, meaning a quick check of what the app currently provides.

Expected results:
- `GET /` returns `200` and the body contains `status: ok`
- `GET /health` returns `200` and the body contains `status: ok`
- `GET /no-such-route` returns `404`

## What was learned in this section

- How to create requests in Postman
- How to use environments to quickly change URLs
- How to write basic tests for responses
- How to export collections and environments to keep as evidence
