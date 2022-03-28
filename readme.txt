Allure Report Package:
allure-behave

for generating allure report:
behave --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports

-o: for folder
-f: for flag
folder shows json files
you have to convert these json to hetml
for these use another package

download from git:
https://github.com/allure-framework/allure2/releases
https://github.com/allure-framework/allure2

cmd:
allure serve <path to allure folder>

