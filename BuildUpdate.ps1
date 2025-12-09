$currentPath = Get-Location
$sources = Get-ChildItem $currentPath -Recurse -Filter "*.css"

$versionTag = Read-Host "Enter new version tag"

foreach ($sourcefile in $sources) {
	python "build-update.py" "$($sourcefile.FullName)" $versionTag
}