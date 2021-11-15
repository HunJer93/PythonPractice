# checkForUserFile.ps1
# Jeremy Hunton
# 10/10/2021\

# define variable containing path to user.txt
$file_location = 'C:\myusers\users.txt'
# check to see if users.txt exists 
$file_exists = Test-Path -Path $file_location
# if the file exists, print out the contents
if ($file_exists -eq $True)
{
    $file_content = Get-Content -Path $file_location
    Write-Output -InputObject $file_content
}
#if the file does not exist, print error message
else 
{
    Write-Output -InputObject "The file users.txt not found!"
}