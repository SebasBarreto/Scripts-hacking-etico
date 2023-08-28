Import-Module ActiveDirectory

Get-ADUser -Filter {Enabled -eq $true} -Properties DisplayName, LastLogonDate | 
Select-Object DisplayName, LastLogonDate | 
Export-Csv -Path "ActiveUsers.csv" -NoTypeInformation

Write-Host "Active users exported to ActiveUsers.csv"
