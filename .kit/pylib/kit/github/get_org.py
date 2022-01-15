from kit import github


def get_org(connection, org_name):
    org = connection.get_organization(org_name)
    github.delay_after_read()
    print(f'Fetched organization {org_name}')
    return org
