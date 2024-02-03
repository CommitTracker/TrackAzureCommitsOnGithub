# Track Azure Devops Commits on Github

**_Description_**

This checks for any pushes to a repo in DevOps and then creates commits in a GitHub repo.

**_Pre Requisites_**

This was created with [Python Version 3.11.7](https://www.python.org/downloads/release/python-3117).  
Make sure you have GitPython installed `pip install GitPython`.  
Create a Personal Access Token in DevOps: [Personal Access Token Guide](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&ranMID=46131&ranEAID=a1LgFw09t88&ranSiteID=a1LgFw09t88-b8iegZkyN9AaABjy9pnSoA&epi=a1LgFw09t88-b8iegZkyN9AaABjy9pnSoA&irgwc=1&OCID=AIDcmm549zy227_aff_7806_1243925&tduid=(ir__zt6irteuakkfdzn3qocuxmistm2x9s63ncaxfnb200)(7806)(1243925)(a1LgFw09t88-b8iegZkyN9AaABjy9pnSoA)()&irclickid=_zt6irteuakkfdzn3qocuxmistm2x9s63ncaxfnb200&tabs=Windows).  
Make sure to give the Token **Code Read** access.

**_How To Use_**

- Create and clone a fork of this repository.
- Open app settings and update it with relevant information: `https://dev.azure.com/{yourOrganization}/{yourProject}/_git/{yourRepo}`
- If you are having package issues run the [`installer.bat`](https://github.com/illuminat3/TrackAzureCommitsOnGithub/blob/main/installer.bat) script.


