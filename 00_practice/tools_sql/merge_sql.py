sqls = [
    'acx_cu_role_0326.sql',
    'ac_cu_authority_0326.sql',
    'acx_cu_role_authority_0326.sql',
    'acx_retailer_role_0326.sql',
    'acx_retailer_authority_0326.sql',
    'acx_retailer_role_authority_0326.sql',
    'ac_cu_role_privilege_0326.sql',
    'ac_cu_route_api_relation_0326.sql',
]
sql_s = '''
TRUNCATE table acx_cu_role;
TRUNCATE table ac_cu_authority;
TRUNCATE table acx_cu_role_authority;
TRUNCATE table acx_retailer_role;
TRUNCATE table acx_retailer_authority;
TRUNCATE table acx_retailer_role_authority;
TRUNCATE table ac_cu_role_privilege;
TRUNCATE table ac_cu_route_api_relation;
'''
for s in sqls:
    with open(s, 'r', encoding='utf-8') as fr:
        sql_s += fr.read()
        sql_s += '\n'

with open('all.sql', 'w', encoding='utf-8') as fw:
    fw.write(sql_s)