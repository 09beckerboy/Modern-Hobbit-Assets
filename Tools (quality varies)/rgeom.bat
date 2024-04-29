@echo off
pushd "%~dp0"

for %%i in (*.rgeom) do (
    set "inputFile=%%~nxi"
    set "outputFile=%%~ni.obj"
    rgeom2obj.exe "!inputFile!" "!outputFile!"
)

popd
