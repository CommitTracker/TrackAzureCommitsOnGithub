Azure To Devops Commit

<b><i>Description</i></b>

This checks for any pushes to a repo in devops and then creates commits in a github repo.

<b><i>Pre Requisites</i></b>

This was created with [Python Version 3.11.7](https://www.python.org/downloads/release/python-3117)

Make sure you have GitPython installed ```pip install GitPython```

Create a Personal Access Token in devops: [Personal Access Token Guide](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&ranMID=46131&ranEAID=a1LgFw09t88&ranSiteID=a1LgFw09t88-b8iegZkyN9AaABjy9pnSoA&epi=a1LgFw09t88-b8iegZkyN9AaABjy9pnSoA&irgwc=1&OCID=AIDcmm549zy227_aff_7806_1243925&tduid=(ir__zt6irteuakkfdzn3qocuxmistm2x9s63ncaxfnb200)(7806)(1243925)(a1LgFw09t88-b8iegZkyN9AaABjy9pnSoA)()&irclickid=_zt6irteuakkfdzn3qocuxmistm2x9s63ncaxfnb200&tabs=Windows)

Make sure to give the Token <b>Code Read</b> access

<b><i>How To Use</i></b>

Create and clone a fork of this repository.

Open app settings and update it with relevant information. 

https://dev.azure.com/{yourOrganization}/{yourProject}/_git/{yourRepo} 

