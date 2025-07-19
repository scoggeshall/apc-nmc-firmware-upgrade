@echo off
REM WinSCP upload for SUMX firmware
REM Usage: sumx_bat.bat ip ftp_user ftp_pass winscp_com_path firmware_file_path log_file_path

if "%~6"=="" (
  echo Usage: %~nx0 ip ftp_user ftp_pass winscp_com_path firmware_file log_file
  exit /b 1
)

set "IP=%~1"
set "USER=%~2"
set "PASS=%~3"
set "WINSCP_COM=%~4"
set "FW_FILE=%~5"
set "LOG_FILE=%~6"

"%WINSCP_COM%" /ini=nul /log="%LOG_FILE%" /command ^
  "option batch abort" ^
  "option confirm off" ^
  "open ftp://%USER%:%PASS%@%IP%" ^
  "put ""%FW_FILE%""" ^
  "exit"

exit /b %ERRORLEVEL%
