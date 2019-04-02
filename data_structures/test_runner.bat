rmdir /s /q .test_runner
mkdir .test_runner

REM tests + coverage
coverage run -m unittest tests.%1Test
coverage report -m
coverage html

start htmlcov\index.html

REM mutation testing
python D:\Users\mdime\Documents\mutpy\bin\mut.py ^
--target src.%1 ^
--unit-test tests.%1Test ^
--report-html .test_runner ^
--coverage

start .test_runner\index.html