#!/usr/bin/env python3
"""
Smoke test for social-post-api package.
Run after building or installing to verify the package works.
No API key required.
"""
import sys


def main():
    print("Smoke test: social-post-api")
    try:
        from ayrshare import SocialPost
        print("  OK: import ayrshare.SocialPost")
    except ImportError as e:
        print("  FAIL: could not import ayrshare.SocialPost:", e)
        return 1

    try:
        # Instantiate with a placeholder key (we only check that the class works)
        s = SocialPost("test-key")
        assert s is not None
        print("  OK: SocialPost() instantiation")
    except Exception as e:
        print("  FAIL: SocialPost() instantiation:", e)
        return 1

    try:
        # Check that expected method exists
        assert hasattr(s, "post") and callable(getattr(s, "post"))
        print("  OK: SocialPost has expected methods (e.g. post)")
    except AssertionError as e:
        print("  FAIL: expected methods missing:", e)
        return 1

    print("Smoke test passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
