# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 언어 지침

모든 응답과 설명은 반드시 **한국어**로 작성한다. 코드 주석, 변수명 등 코드 자체는 예외이나, 사용자에게 전달하는 모든 텍스트는 한글을 사용한다.

## Project

A single-file static web calculator (`calculator.html`). No build step, no dependencies, no package manager — open the file directly in a browser to run it.

## Architecture

Everything lives in `calculator.html` as inline `<style>` and `<script>`:

- **Display** — shows the current value and the running expression history
- **Keypad** — 4×5 grid of buttons; event delegation on `.keypad` handles all clicks via `data-action` / `data-digit` / `data-op` attributes
- **State** — four plain variables (`current`, `previous`, `operator`, `justCalculated`) drive all logic; no framework
- **3D effect** — CSS `box-shadow` layering + `perspective` + `mousemove` parallax; no canvas or WebGL
