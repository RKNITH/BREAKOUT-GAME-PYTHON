run:
	cls
	@powershell write-host -fore Yellow Run project with scriptfile...
	@python .\main.py


test:
	cls
	@powershell write-host -fore Yellow Run PyTest ...
	@pytest
	@powershell write-host -fore Green PyTest finished!

clean:
	cls
	@powershell write-host -fore Yellow Clean up project files...
	@if exist ".\build" rd /q /s build
	@if exist ".\dist" rd /q /s dist
	@if exist ".pytest_cache" rd /q /s .pytest_cache 
	@if exist ".\src\__pycache__" rd /q /s .\src\__pycache__
	@if exist ".\tests\__pycache__" rd /q /s .\tests\__pycache__
	@powershell write-host -fore Green Clean up finished!

build:
	cls
	@powershell write-host -fore Yellow Start building process...
	@pyinstaller .\config\main.spec
	@explorer .\dist\BreakOut
	@.\config\ForgeProject.ifp
	@powershell write-host -fore Green Build is finished!

pack:
	cls
	@powershell write-host -fore Yellow Start packaging process...
	@move .\package\Setup-BreakOut-PyGame.exe .
	@tar.exe -a -c -f BreakOut-PyGame.zip Setup-BreakOut-PyGame.exe
	@move .\BreakOut-PyGame.zip .\package
	@move .\Setup-BreakOut-PyGame.exe .\package  
	@powershell write-host -fore Green Packaging done!
