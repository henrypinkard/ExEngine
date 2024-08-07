# src/exengine/integration_tests/test_imports.py

import pytest


def test_import_engine():
    try:
        from exengine import ExecutionEngine
    except ImportError as e:
        pytest.fail(f"Import failed for ExecutionEngine: {e}")

def test_import_base_classes():
    try:
        from exengine.base_classes import Notification, ExecutorEvent
    except ImportError as e:
        pytest.fail(f"Import failed for base_classes: {e}")

def test_import_notifications():
    try:
        from exengine.notifications import NotificationCategory, DataStoredNotification, EventExecutedNotification
    except ImportError as e:
        pytest.fail(f"Import failed for notifications: {e}")
