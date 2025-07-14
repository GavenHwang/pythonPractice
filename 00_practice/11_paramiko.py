import paramiko


def connect_and_execute_command(host, port, username, password, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=port, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode('utf - 8')
        error = stderr.read().decode('utf - 8')
        if error:
            print(f"命令执行出错: {error}")
        else:
            print(f"命令执行结果: {output}")
    except paramiko.AuthenticationException:
        print("认证失败，请检查用户名和密码。")
    except paramiko.SSHException as ssh_ex:
        print(f"SSH连接出现问题: {ssh_ex}")
    except Exception as ex:
        print(f"出现其他错误: {ex}")
    finally:
        ssh.close()


def upload_file(host, port, username, password, local_path, remote_path):
    transport = paramiko.Transport((host, port))
    try:
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        try:
            sftp.put(local_path, remote_path)
            print(f"文件 {local_path} 上传成功到 {remote_path}")
        except FileNotFoundError:
            print(f"本地文件 {local_path} 未找到。")
        except PermissionError:
            print(f"没有权限上传文件到 {remote_path}。")
        finally:
            sftp.close()
    except paramiko.AuthenticationException:
        print("认证失败，请检查用户名和密码。")
    except paramiko.SSHException as ssh_ex:
        print(f"SSH连接出现问题: {ssh_ex}")
    except Exception as ex:
        print(f"出现其他错误: {ex}")
    finally:
        transport.close()


def download_file(host, port, username, password, remote_path, local_path):
    transport = paramiko.Transport((host, port))
    try:
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        try:
            sftp.get(remote_path, local_path)
            print(f"文件 {remote_path} 下载成功到 {local_path}")
        except FileNotFoundError:
            print(f"远程文件 {remote_path} 未找到。")
        except PermissionError:
            print(f"没有权限下载文件 {remote_path}。")
        finally:
            sftp.close()
    except paramiko.AuthenticationException:
        print("认证失败，请检查用户名和密码。")
    except paramiko.SSHException as ssh_ex:
        print(f"SSH连接出现问题: {ssh_ex}")
    except Exception as ex:
        print(f"出现其他错误: {ex}")
    finally:
        transport.close()


if __name__ == "__main__":
    host = "your_server_ip"
    port = 22
    username = "your_username"
    password = "your_password"
    command = "ls -l"
    remote_path = "/path/to/remote/file.txt"
    local_path = "/path/to/local/file.txt"
    connect_and_execute_command(host, port, username, password, command)
    upload_file(host, port, username, password, local_path, remote_path)
    download_file(host, port, username, password, remote_path, local_path)
