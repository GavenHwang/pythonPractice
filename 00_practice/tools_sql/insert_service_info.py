# -*- coding: utf-8 -*-
import pymysql

# 服务信息('服务名称', '类型(默认版本获取路径为1，自定义版本获取路径为2)', '路径拼接', '1：平台端；2集群端；3：部署在集群端给平台端使用')
service_info = [
    # 平台端
    ('acm', '2', '/ui/acm', '1'),
    ('sacp', '2', '/ac', '1'),
    ('easyop', '2', '/itos', '1'),
    ('sso', '2', '/sso', '1'),
    ('message', '2', '/acx/message', '1'),
    ('admin-ui', '2', '/ui/admin', '1'),
    ('aihub-ui', '2', '/ui/aihub', '1'),
    ('console-ui', '2', '/ui/console', '1'),
    ('mall-ui', '2', '/ui/mall', '1'),
    ('seller-ui', '2', '/ui/seller', '1'),
    ('chatbot-ui', '2', '/ui/chatbot', '1'),
    ('llm-ui', '2', '/ui/llm', '1'),
    ('ac-openapi', '2', '/ac/openapi', '1'),
    ('acx-aihub', '1', '', '1'),
    ('acx-aimgt', '1', '', '1'),
    ('acx-appcenter', '1', '', '1'),
    ('acx-baremetal', '1', '', '1'),
    ('acx-bizanalysis', '1', '', '1'),
    ('acx-business', '1', '', '1'),
    ('acx-charge', '1', '', '1'),
    ('acx-customerservice', '1', '', '1'),
    ('acx-desktopcenter', '1', '', '1'),
    ('acx-dptech-bill-oss', '3', '', '1'),
    ('acx-fund', '1', '', '1'),
    ('acx-gateway', '1', '', '1'),
    ('acx-internalproxy', '3', '', '1'),
    ('acx-jobgather', '1', '', '1'),
    ('acx-jobmgt', '1', '', '1'),
    ('acx-learning', '1', '', '1'),
    ('acx-mall', '1', '', '1'),
    ('acx-market', '1', '', '1'),
    ('acx-network', '1', '', '1'),
    ('acx-operation', '1', '', '1'),
    ('acx-pay', '1', '', '1'),
    ('acx-platform', '1', '', '1'),
    ('acx-resource', '1', '', '1'),
    ('acx-search', '1', '', '1'),
    ('acx-user', '1', '', '1'),
    ('acx-videomonitor', '3', '', '1'),
    ('acx-wechat', '1', '', '1'),
    ('acx-chatbot', '1', '', '1'),
    ('acx-llm', '1', '', '1'),
    ('acx-clusterop', '1', '', '1'),
    # 集群端
    ('gv', '2', '/login/getVersion.action', '2'),
    ('efile', '1', '', '2'),
    ('eshell', '1', '', '2'),
    ('gv-openapi', '2', '/hpc/openapi', '2'),
    ('acx-alarm', '1', '', '2'),
    ('acx-appagent', '1', '', '2'),
    ('acx-clustermonitor', '1', '', '2'),
    ('acx-cmdb', '1', '', '2'),
    ('acx-collector', '1', '', '2'),
    ('acx-containermgt', '1', '', '2'),
    ('acx-dataasset', '1', '', '2'),
    ('acx-desktopagent', '1', '', '2'),
    ('acx-gateway', '3', '', '2'),
    ('acx-imagemgt', '1', '', '2'),
    ('acx-inference', '1', '', '2'),
    ('acx-jobsched', '1', '', '2'),
    ('acx-packageagent', '1', '', '2'),
    ('acx-platform', '1', '', '2'),
    ('acx-storagemgt', '1', '', '2'),
    ('acx-useragent', '1', '', '2'),
    ('acx-clustermgt', '1', '', '2'),
    # 部署在集群端给平台端使用的组件
    ('acx-repoagent', '1', '', '3'),
    ('repo-efile', '1', '', '3'),
]


def insert_service_info():
    # 连接到 MySQL 数据库
    conn = pymysql.connect(host='10.0.36.102', port=3309, user='root', password='root123', database='ac_diff')
    # 创建游标对象
    cursor = conn.cursor()
    try:
        # 清空表
        truncate_sql = "TRUNCATE table service_info;"
        cursor.execute(truncate_sql)
        print(f"{truncate_sql} 执行成功")
        conn.commit()
        # 插入数据
        index = 20000
        for i in service_info:
            insert_sql = f"""INSERT INTO `ac_diff`.`service_info` (`id`, `service_name`, `service_type`, `extra_path`, `platform_type`) VALUES ({index}, '{i[0]}', '{i[1]}', '{i[2]}', '{i[3]}')"""
            cursor.execute(insert_sql)
            conn.commit()
            print(f"{insert_sql} 执行成功")
            index += 1
    except pymysql.Error as e:
        print(f"插入数据时出错: {e}")
    finally:
        # 关闭游标和连接
        cursor.close()
        conn.close()


if __name__ == '__main__':
    insert_service_info()
