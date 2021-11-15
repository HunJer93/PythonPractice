# workWithFiles4.ps1
# The purpose of this program is to practice getting contents of files with PowerShell
# Jeremy Hunton
# 10/10/21

# define the paths for dognames.txt and catnames.txt
$file_path_dogs = 'C:\cpt180Stuff\pets\dogs\dognames.txt'
$file_path_cats = 'C:\cpt180Stuff\pets\cats\catnames.txt'
#check to see if both files exist
$dogs_exist = Test-Path -Path $file_path_dogs
$cats_exist = Test-Path -Path $file_path_cats
# determine if the dognames.txt file and the catnames.txt file exist
if ($dogs_exist -eq $True -AND $cats_exist -eq $True)
{
    #get the contents of the file dognames.txt and print it
    Get-Content -Path $file_path_dogs | Write-Host

    # add a space to keep the lists separate
    Write-Output -InputObject ''

    # get the contents of the file catnames.txt and print it
    Get-Content -Path $file_path_cats | Write-Host

    # add two cat names to the catnames.txt file
    Add-Content -Path $file_path_cats -Value 'Katy Purry'
    Add-Content -Path $file_path_cats -Value 'Walter Croncat'

    # add  a space to keep the lists separate
    Write-Output -InputObject ''

    # reprint the catnames.txt
    Get-Content -Path $file_path_cats | Write-Host

 
} # end both files exist
else
{
    Write-Output -InputObject 'Unable to access one or more files.'
}# end one or more files does not exist    

# Question: What is a PowerShell pipeline? Show an example
# Answer: A PowerShell pipeline is a way to connect Cmdlets together so you can do multiple commands at the same time. An example of this is on 
# line 22 and 32. The first Cmdlet being used is 'Get-Content' which gets the content of the file path given in both instances. Using the pipe operator "|", we are 
# able to then call the command 'Write-Host' to write the contents of the file to the screen. 