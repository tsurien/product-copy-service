# pytest가 이 폴더를 프로젝트 루트로 인식하게 한다 (app 패키지 import용)

# Keep the separate order TDD exercise out of app CI.
collect_ignore = ["tests/test_order.py"]
