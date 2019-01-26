@echo off

for /r %%i in (ninja.exe) do (
	if exist %%i echo %%i
)
