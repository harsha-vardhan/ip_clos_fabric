

spine_11_ls = [('spine-11', 'et-0/0/1', 'leaf-12', 'et-0/0/48'), ('spine-11', 'et-0/0/0', 'leaf-11', 'et-0/0/48'), ('spine-11', 'et-0/0/2', 'leaf-13', 'et-0/0/48'), ('spine-11', 'et-0/0/3', 'leaf-14', 'et-0/0/48')]

spine_12_ls = [('spine-12', 'et-0/0/0', 'leaf-11', 'et-0/0/49'), ('spine-12', 'et-0/0/2', 'leaf-13', 'et-0/0/49'), ('spine-12', 'et-0/0/3', 'leaf-14', 'et-0/0/49'), ('spine-12', 'et-0/0/1', 'leaf-12', 'et-0/0/49')]


spine_11_bgp = [('spine-11', '400', '192.169.0.1'), ('spine-11', '401', '192.169.0.3'), ('spine-11', '402', '192.169.0.5'), ('spine-11', '403', '192.169.0.7')]

spine_12_bgp = [('spine-12', '400', '192.169.0.9'), ('spine-12', '401', '192.169.0.11'), ('spine-12', '402', '192.169.0.13'), ('spine-12', '403', '192.169.0.15')]

leaf_gw = {'leaf-11' : '172.17.0.1', 'leaf-12' : '172.17.1.1', 'leaf-13' : '172.17.2.1', 'leaf-14' : '172.17.3.1'}

leaf_devices = ['leaf-11', 'leaf-12', 'leaf-13', 'leaf-14']

device_details = {'spine-11' : {'mgmt_ip'  : '172.32.32.201',
      				 'port'     : '22',
                                 'username' : 'root',
                                 'password' : 'password'
                                },
                  'spine-12' : {'mgmt_ip'  : '172.32.32.202',
                                 'port'     : '22',
                                 'username' : 'root',
                                 'password' : 'password'
                                },
                  'leaf-11' : {'mgmt_ip'  : '172.32.32.101',
                                 'port'     : '22',
                                 'username' : 'root',
                                 'password' : 'password'
                                },
                  'leaf-12' : {'mgmt_ip'  : '172.32.32.102',
                                 'port'     : '22',
                                 'username' : 'root',
                                 'password' : 'password'
                                },
                  'leaf-13' : {'mgmt_ip'  : '172.32.32.103',
                                 'port'     : '22',
                                 'username' : 'root',
                                 'password' : 'password'
                                },
                  'leaf-14' : {'mgmt_ip'  : '172.32.32.104',
                                 'port'     : '22',
                                 'username' : 'root',
                                 'password' : 'password'
                                }
                  }
