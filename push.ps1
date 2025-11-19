git init
git config user.name "Suyog"
git config user.email "yadavsuyog623@gmail.com"
git add -A
git commit -m "Initial portfolio commit"

$username = Read-Host "Enter GitHub username"
$repo = Read-Host "Enter repository name"
$token = Read-Host "Enter GitHub Personal Access Token"

git remote add origin "https://$username`:$token@github.com/$username/$repo.git"
git branch -M main
git push -u origin main

Write-Host "Done! Check GitHub for your uploaded files."
