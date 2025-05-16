# Ignore library warnings
# These are false positives in library code that we don't control

# Ignore Altair methods (library)
sampleUniform = cumulativeUniform = densityUniform = None

# Ignore urllib3 unused variables (library)
SUCCESS_EOF = None
onmessage = None
_is_done = None
responseType = None

# Ignore urllib3 poolmanager unused variables (library)
key_scheme = key_host = key_port = key_timeout = None
key_retries = key_block = key_source_address = None
key_key_file = key_key_password = key_cert_file = None
key_cert_reqs = key_ca_certs = key_ca_cert_data = None
key_ssl_version = key_ssl_minimum_version = None
key_ssl_maximum_version = key_ca_cert_dir = key_ssl_context = None
key_maxsize = key_headers = key__proxy = key__proxy_headers = None
key__proxy_config = key_socket_options = key__socks_options = None
key_assert_hostname = key_assert_fingerprint = None
key_server_hostname = key_blocksize = None

# Ignore yaml unused functions (library)
compose_all = full_load = full_load_all = None
safe_load_all = unsafe_load = unsafe_load_all = None
safe_dump_all = None

# Ignore project-specific unused items
# These are false positives in our code
motion_generator = None

# Ignore unused parsing functions (they are used dynamically)
parse_pylint = parse_mypy = parse_bandit = None
parse_flake8 = parse_vulture = None
