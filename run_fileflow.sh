#!/bin/bash

docker run --rm \
  -v "$(pwd)/input:/app/input" \
    -v "$(pwd)/processed:/app/processed" \
      -v "$(pwd)/quarantine:/app/quarantine" \
        -v "$(pwd)/logs:/app/logs" \
          -v "$(pwd)/reports:/app/reports" \
            -v "$(pwd)/archive:/app/archive" \
              fileflow
              