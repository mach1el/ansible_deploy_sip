#!/bin/bash
psql -h localhost -U opensips -d opensips -c "truncate acc RESTART IDENTITY CASCADE;"