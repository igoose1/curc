#!/bin/sh

printf "git tag: %s\n" "$(git describe --tags)"
printf "curc version: %s\n" "$(uv run python -c 'import curc; print(curc.__version__)')"
read -rp "Are you sure you want to publish that? (y/n) " choice
if [ "$choice" = y ]; then
	rm -rf dist
	uv build
	uv publish
fi
