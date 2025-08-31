<style>
    ul {
        padding-left: 12px;
    }
    li {
        padding-left: 12px;
    }
    ul.bullet li.dir {
        list-style-type: circle
    }
    ul.bullet li.fil {
        list-style-type: disc;
    }
    ul.dashed li.dir {
        list-style-type: none;
    }
    ul.dashed li.fil {
        list-style-type: none;
    }
    ul.dashed li.fil::before {
        content: "-";

    }
    ul.dashed li.dir summary::before {
        content: "+";
    }
    ol {
        padding-left: 12px;
    }
    a.deadlink {
        font-weight: bold;
    }
    a.pagenav {
        text-decoration: underline;
    }
    summary {
        list-style: none; /* Ensures no default marker is shown */
        position: relative; /* Needed for absolute positioning of the custom arrow */
        padding-right: 20px; /* Adjust as needed to make space for the arrow */
        cursor: pointer; /* Indicates it's clickable */
    }

    summary::after {
        content: '▶'; /* Unicode character for a right-pointing triangle */
        transform: translateY(-50%); /* Vertically centers the arrow */
        transition: transform 0.2s ease-in-out;
    }

    details[open] summary::after {
        content: '▼'; /* Unicode character for a down-pointing triangle when open */
    }
</style>
<ul class="bullet">
    <li class="dir">
        <details open>
            <summary>
                <a class="deadlink">
                    3d Scanner
                </a>
                <a class="pagenav" href="/3d_scanner/3d_scanner/3d_scanner.md">
                    (page)
                </a>
            </summary>
            <ul>
                <ul>
                    <li class="dir">
                        <details open>
                            <summary>
                                <a class="deadlink">
                                    Electrical Connectors
                                </a>
                                <a class="pagenav" href="/3d_scanner/electrical_connectors/electrical_connectors/electrical_connectors.md">
                                    (page)
                                </a>
                            </summary>
                            <ul>
                                <ul>
                                    <li class="dir">
                                        <details>
                                            <summary>
                                                <a class="deadlink">
                                                    Pictures
                                                </a>
                                                <a class="pagenav" href="/3d_scanner/electrical_connectors/pictures/pictures/pictures.md">
                                                    (page)
                                                </a>
                                            </summary>
                                            <ul>
                                                <ul></ul>
                                            </ul>
                                        </details>
                                    </li>
                                    <li class="fil">
                                        <a href="/3d_scanner/electrical_connectors/deutsch.md">
                                            Deutsch
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/3d_scanner/electrical_connectors/dupont.md">
                                            Dupont
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/3d_scanner/electrical_connectors/jst.md">
                                            Jst
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/3d_scanner/electrical_connectors/micro_usb.md">
                                            Micro Usb
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/3d_scanner/electrical_connectors/qwiic.md">
                                            Qwiic
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/3d_scanner/electrical_connectors/usbc.md">
                                            Usbc
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/3d_scanner/electrical_connectors/usb_a.md">
                                            Usb A
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/3d_scanner/electrical_connectors/usb_b.md">
                                            Usb B
                                        </a>
                                    </li>
                                </ul>
                            </ul>
                        </details>
                    </li>
                    <li class="dir">
                        <details open>
                            <summary>
                                <a class="deadlink">
                                    Physical Communication Protocols
                                </a>
                                <a class="pagenav" href="/3d_scanner/physical_communication_protocols/physical_communication_protocols/physical_communication_protocols.md">
                                    (page)
                                </a>
                            </summary>
                            <ul>
                                <ul>
                                    <li class="fil">
                                        <a href="/3d_scanner/physical_communication_protocols/can.md">
                                            Can
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/3d_scanner/physical_communication_protocols/i2c.md">
                                            I2c
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/3d_scanner/physical_communication_protocols/rs_232.md">
                                            Rs 232
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/3d_scanner/physical_communication_protocols/rs_485.md">
                                            Rs 485
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/3d_scanner/physical_communication_protocols/serial.md">
                                            Serial
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/3d_scanner/physical_communication_protocols/ttl.md">
                                            Ttl
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/3d_scanner/physical_communication_protocols/uart.md">
                                            Uart
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/3d_scanner/physical_communication_protocols/usb_can.md">
                                            Usb Can
                                        </a>
                                    </li>
                                </ul>
                            </ul>
                        </details>
                    </li>
                    <li class="dir">
                        <details open>
                            <summary>
                                <a class="deadlink">
                                    Sensors
                                </a>
                                <a class="pagenav" href="/3d_scanner/sensors/sensors/sensors.md">
                                    (page)
                                </a>
                            </summary>
                            <ul>
                                <ul>
                                    <li class="fil">
                                        <a href="/3d_scanner/sensors/berryimuv3.md">
                                            Berryimuv3
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/3d_scanner/sensors/bno055.md">
                                            Bno055
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/3d_scanner/sensors/gt_u7_gps.md">
                                            Gt U7 Gps
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/3d_scanner/sensors/rpi_cam_module_v2_8mp.md">
                                            Rpi Cam Module V2 8mp
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/3d_scanner/sensors/rplidar_a1m8.md">
                                            Rplidar A1m8
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/3d_scanner/sensors/vl53l1x.md">
                                            Vl53l1x
                                        </a>
                                    </li>
                                </ul>
                            </ul>
                        </details>
                    </li>
                    <li class="fil">
                        <a href="/3d_scanner/3d_scanner.md">
                            3d Scanner
                        </a>
                    </li>
                    <li class="fil">
                        <a href="/3d_scanner/piz_uptime_plus.md">
                            Piz Uptime Plus
                        </a>
                    </li>
                    <li class="fil">
                        <a href="/3d_scanner/rpi_4.md">
                            Rpi 4
                        </a>
                    </li>
                </ul>
            </ul>
        </details>
    </li>
    <li class="dir">
        <details open>
            <summary>
                <a class="deadlink">
                    Bookmarks
                </a>
                <a class="pagenav" href="/bookmarks/bookmarks/bookmarks.md">
                    (page)
                </a>
            </summary>
            <ul>
                <ul>
                    <li class="fil">
                        <a href="/bookmarks/markdown_tools.md">
                            Markdown Tools
                        </a>
                    </li>
                </ul>
            </ul>
        </details>
    </li>
    <li class="dir">
        <details open>
            <summary>
                <a class="deadlink">
                    Core Concepts
                </a>
                <a class="pagenav" href="/core_concepts/core_concepts/core_concepts.md">
                    (page)
                </a>
            </summary>
            <ul>
                <ul>
                    <li class="dir">
                        <details open>
                            <summary>
                                <a class="deadlink">
                                    Computers
                                </a>
                                <a class="pagenav" href="/core_concepts/computers/computers/computers.md">
                                    (page)
                                </a>
                            </summary>
                            <ul>
                                <ul>
                                    <li class="fil">
                                        <a href="/core_concepts/computers/bios.md">
                                            Bios
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/computers/components.md">
                                            Components
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/computers/drivers.md">
                                            Drivers
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/computers/hardware.md">
                                            Hardware
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/computers/kernel.md">
                                            Kernel
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/computers/software.md">
                                            Software
                                        </a>
                                    </li>
                                </ul>
                            </ul>
                        </details>
                    </li>
                    <li class="dir">
                        <details open>
                            <summary>
                                <a class="deadlink">
                                    Development
                                </a>
                                <a class="pagenav" href="/core_concepts/development/development/development.md">
                                    (page)
                                </a>
                            </summary>
                            <ul>
                                <ul>
                                    <li class="dir">
                                        <details>
                                            <summary>
                                                <a class="deadlink">
                                                    Cryptography
                                                </a>
                                                <a class="pagenav" href="/core_concepts/development/cryptography/cryptography/cryptography.md">
                                                    (page)
                                                </a>
                                            </summary>
                                            <ul>
                                                <ul>
                                                    <li class="dir">
                                                        <details>
                                                            <summary>
                                                                <a class="deadlink">
                                                                    Certificates
                                                                </a>
                                                                <a class="pagenav" href="/core_concepts/development/cryptography/certificates/certificates/certificates.md">
                                                                    (page)
                                                                </a>
                                                            </summary>
                                                            <ul>
                                                                <ul>
                                                                    <li class="fil">
                                                                        <a href="/core_concepts/development/cryptography/certificates/certificate_signing.md">
                                                                            Certificate Signing
                                                                        </a>
                                                                    </li>
                                                                    <li class="fil">
                                                                        <a href="/core_concepts/development/cryptography/certificates/cert_chain.md">
                                                                            Cert Chain
                                                                        </a>
                                                                    </li>
                                                                    <li class="fil">
                                                                        <a href="/core_concepts/development/cryptography/certificates/root_ca.md">
                                                                            Root Ca
                                                                        </a>
                                                                    </li>
                                                                    <li class="fil">
                                                                        <a href="/core_concepts/development/cryptography/certificates/x509.md">
                                                                            X509
                                                                        </a>
                                                                    </li>
                                                                </ul>
                                                            </ul>
                                                        </details>
                                                    </li>
                                                    <li class="dir">
                                                        <details>
                                                            <summary>
                                                                <a class="deadlink">
                                                                    Web Cert Examples
                                                                </a>
                                                                <a class="pagenav" href="/core_concepts/development/cryptography/web_cert_examples/web_cert_examples/web_cert_examples.md">
                                                                    (page)
                                                                </a>
                                                            </summary>
                                                            <ul>
                                                                <ul>
                                                                    <li class="fil">
                                                                        <a href="/core_concepts/development/cryptography/web_cert_examples/pkcs_1_sha-256_with_rsa_encryption.md">
                                                                            Pkcs 1 Sha 256 With Rsa Encryption
                                                                        </a>
                                                                    </li>
                                                                    <li class="fil">
                                                                        <a href="/core_concepts/development/cryptography/web_cert_examples/x9.62_ecdsa_with_sha-256.md">
                                                                            X9 62 Ecdsa With Sha 256
                                                                        </a>
                                                                    </li>
                                                                </ul>
                                                            </ul>
                                                        </details>
                                                    </li>
                                                    <li class="fil">
                                                        <a href="/core_concepts/development/cryptography/certificates.md">
                                                            Certificates
                                                        </a>
                                                    </li>
                                                    <li class="fil">
                                                        <a href="/core_concepts/development/cryptography/encryption.md">
                                                            Encryption
                                                        </a>
                                                    </li>
                                                    <li class="fil">
                                                        <a href="/core_concepts/development/cryptography/hashing.md">
                                                            Hashing
                                                        </a>
                                                    </li>
                                                    <li class="fil">
                                                        <a href="/core_concepts/development/cryptography/salting.md">
                                                            Salting
                                                        </a>
                                                    </li>
                                                </ul>
                                            </ul>
                                        </details>
                                    </li>
                                    <li class="dir">
                                        <details>
                                            <summary>
                                                <a class="deadlink">
                                                    Languages
                                                </a>
                                                <a class="pagenav" href="/core_concepts/development/languages/languages/languages.md">
                                                    (page)
                                                </a>
                                            </summary>
                                            <ul>
                                                <ul>
                                                    <li class="dir">
                                                        <details>
                                                            <summary>
                                                                <a class="deadlink">
                                                                    Javascript
                                                                </a>
                                                                <a class="pagenav" href="/core_concepts/development/languages/javascript/javascript/javascript.md">
                                                                    (page)
                                                                </a>
                                                            </summary>
                                                            <ul>
                                                                <ul>
                                                                    <li class="fil">
                                                                        <a href="/core_concepts/development/languages/javascript/angular.md">
                                                                            Angular
                                                                        </a>
                                                                    </li>
                                                                    <li class="fil">
                                                                        <a href="/core_concepts/development/languages/javascript/nodejs.md">
                                                                            Nodejs
                                                                        </a>
                                                                    </li>
                                                                    <li class="fil">
                                                                        <a href="/core_concepts/development/languages/javascript/react.md">
                                                                            React
                                                                        </a>
                                                                    </li>
                                                                </ul>
                                                            </ul>
                                                        </details>
                                                    </li>
                                                    <li class="dir">
                                                        <details>
                                                            <summary>
                                                                <a class="deadlink">
                                                                    Python
                                                                </a>
                                                                <a class="pagenav" href="/core_concepts/development/languages/python/python/python.md">
                                                                    (page)
                                                                </a>
                                                            </summary>
                                                            <ul>
                                                                <ul>
                                                                    <li class="dir">
                                                                        <details>
                                                                            <summary>
                                                                                <a class="deadlink">
                                                                                    Flask
                                                                                </a>
                                                                                <a class="pagenav" href="/core_concepts/development/languages/python/flask/flask/flask.md">
                                                                                    (page)
                                                                                </a>
                                                                            </summary>
                                                                            <ul>
                                                                                <ul>
                                                                                    <li class="fil">
                                                                                        <a href="/core_concepts/development/languages/python/flask/flask_jwt.md">
                                                                                            Flask Jwt
                                                                                        </a>
                                                                                    </li>
                                                                                    <li class="fil">
                                                                                        <a href="/core_concepts/development/languages/python/flask/flask_sqlalchemy.md">
                                                                                            Flask Sqlalchemy
                                                                                        </a>
                                                                                    </li>
                                                                                    <li class="fil">
                                                                                        <a href="/core_concepts/development/languages/python/flask/hosting_with_cherrypy.md">
                                                                                            Hosting With Cherrypy
                                                                                        </a>
                                                                                    </li>
                                                                                    <li class="fil">
                                                                                        <a href="/core_concepts/development/languages/python/flask/hosting_with_gunicorn.md">
                                                                                            Hosting With Gunicorn
                                                                                        </a>
                                                                                    </li>
                                                                                </ul>
                                                                            </ul>
                                                                        </details>
                                                                    </li>
                                                                    <li class="fil">
                                                                        <a href="/core_concepts/development/languages/python/flask.md">
                                                                            Flask
                                                                        </a>
                                                                    </li>
                                                                    <li class="fil">
                                                                        <a href="/core_concepts/development/languages/python/sqlalchemy.md">
                                                                            Sqlalchemy
                                                                        </a>
                                                                    </li>
                                                                </ul>
                                                            </ul>
                                                        </details>
                                                    </li>
                                                    <li class="fil">
                                                        <a href="/core_concepts/development/languages/javascript.md">
                                                            Javascript
                                                        </a>
                                                    </li>
                                                    <li class="fil">
                                                        <a href="/core_concepts/development/languages/python.md">
                                                            Python
                                                        </a>
                                                    </li>
                                                </ul>
                                            </ul>
                                        </details>
                                    </li>
                                    <li class="dir">
                                        <details>
                                            <summary>
                                                <a class="deadlink">
                                                    Security
                                                </a>
                                                <a class="pagenav" href="/core_concepts/development/security/security/security.md">
                                                    (page)
                                                </a>
                                            </summary>
                                            <ul>
                                                <ul>
                                                    <li class="fil">
                                                        <a href="/core_concepts/development/security/2_factor_auth.md">
                                                            2 Factor Auth
                                                        </a>
                                                    </li>
                                                    <li class="fil">
                                                        <a href="/core_concepts/development/security/basic_auth.md">
                                                            Basic Auth
                                                        </a>
                                                    </li>
                                                    <li class="fil">
                                                        <a href="/core_concepts/development/security/gpg_keys.md">
                                                            Gpg Keys
                                                        </a>
                                                    </li>
                                                    <li class="fil">
                                                        <a href="/core_concepts/development/security/passkey.md">
                                                            Passkey
                                                        </a>
                                                    </li>
                                                </ul>
                                            </ul>
                                        </details>
                                    </li>
                                    <li class="dir">
                                        <details>
                                            <summary>
                                                <a class="deadlink">
                                                    Setup
                                                </a>
                                                <a class="pagenav" href="/core_concepts/development/setup/setup/setup.md">
                                                    (page)
                                                </a>
                                            </summary>
                                            <ul>
                                                <ul>
                                                    <li class="fil">
                                                        <a href="/core_concepts/development/setup/angular_wsl.md">
                                                            Angular Wsl
                                                        </a>
                                                    </li>
                                                </ul>
                                            </ul>
                                        </details>
                                    </li>
                                    <li class="dir">
                                        <details>
                                            <summary>
                                                <a class="deadlink">
                                                    Tools
                                                </a>
                                                <a class="pagenav" href="/core_concepts/development/tools/tools/tools.md">
                                                    (page)
                                                </a>
                                            </summary>
                                            <ul>
                                                <ul>
                                                    <li class="fil">
                                                        <a href="/core_concepts/development/tools/ide.md">
                                                            Ide
                                                        </a>
                                                    </li>
                                                    <li class="fil">
                                                        <a href="/core_concepts/development/tools/text_editors.md">
                                                            Text Editors
                                                        </a>
                                                    </li>
                                                    <li class="fil">
                                                        <a href="/core_concepts/development/tools/virtualbox.md">
                                                            Virtualbox
                                                        </a>
                                                    </li>
                                                </ul>
                                            </ul>
                                        </details>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/development/character_sets.md">
                                            Character Sets
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/development/cryptography.md">
                                            Cryptography
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/development/database.md">
                                            Database
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/development/encoding.md">
                                            Encoding
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/development/jwt.md">
                                            Jwt
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/development/oauth.md">
                                            Oauth
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/development/orm.md">
                                            Orm
                                        </a>
                                    </li>
                                </ul>
                            </ul>
                        </details>
                    </li>
                    <li class="dir">
                        <details open>
                            <summary>
                                <a class="deadlink">
                                    Linux General
                                </a>
                                <a class="pagenav" href="/core_concepts/linux_general/linux_general/linux_general.md">
                                    (page)
                                </a>
                            </summary>
                            <ul>
                                <ul>
                                    <li class="fil">
                                        <a href="/core_concepts/linux_general/containerization.md">
                                            Containerization
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/linux_general/containers_vs_vms.md">
                                            Containers Vs Vms
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/linux_general/kvm.md">
                                            Kvm
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/linux_general/setting_network_proxy.md">
                                            Setting Network Proxy
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/linux_general/ssh.md">
                                            Ssh
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/linux_general/vnc.md">
                                            Vnc
                                        </a>
                                    </li>
                                </ul>
                            </ul>
                        </details>
                    </li>
                    <li class="dir">
                        <details open>
                            <summary>
                                <a class="deadlink">
                                    Linux Tools
                                </a>
                                <a class="pagenav" href="/core_concepts/linux_tools/linux_tools/linux_tools.md">
                                    (page)
                                </a>
                            </summary>
                            <ul>
                                <ul>
                                    <li class="fil">
                                        <a href="/core_concepts/linux_tools/grep.md">
                                            Grep
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/linux_tools/keytool_cheatsheet.md">
                                            Keytool Cheatsheet
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/linux_tools/nginx.md">
                                            Nginx
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/linux_tools/nslookup.md">
                                            Nslookup
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/linux_tools/openssl.md">
                                            Openssl
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/linux_tools/sed.md">
                                            Sed
                                        </a>
                                    </li>
                                </ul>
                            </ul>
                        </details>
                    </li>
                    <li class="dir">
                        <details open>
                            <summary>
                                <a class="deadlink">
                                    Networking
                                </a>
                                <a class="pagenav" href="/core_concepts/networking/networking/networking.md">
                                    (page)
                                </a>
                            </summary>
                            <ul>
                                <ul>
                                    <li class="fil">
                                        <a href="/core_concepts/networking/7_layer_osi_model.md">
                                            7 Layer Osi Model
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/networking/dhcp.md">
                                            Dhcp
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/networking/dns.md">
                                            Dns
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/networking/firewall.md">
                                            Firewall
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/networking/mac_addresses.md">
                                            Mac Addresses
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/networking/nat.md">
                                            Nat
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/networking/network_device_diagram.md">
                                            Network Device Diagram
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/networking/net_request_full_breakdown.md">
                                            Net Request Full Breakdown
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/networking/packets.md">
                                            Packets
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/networking/proxies.md">
                                            Proxies
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/networking/routers.md">
                                            Routers
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/networking/routing_table.md">
                                            Routing Table
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/networking/spanning_tree.md">
                                            Spanning Tree
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/networking/ssl_tls.md">
                                            Ssl Tls
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/networking/switches_and_hubs.md">
                                            Switches And Hubs
                                        </a>
                                    </li>
                                </ul>
                            </ul>
                        </details>
                    </li>
                    <li class="dir">
                        <details open>
                            <summary>
                                <a class="deadlink">
                                    Storage
                                </a>
                                <a class="pagenav" href="/core_concepts/storage/storage/storage.md">
                                    (page)
                                </a>
                            </summary>
                            <ul>
                                <ul>
                                    <li class="fil">
                                        <a href="/core_concepts/storage/storage.md">
                                            Storage
                                        </a>
                                    </li>
                                </ul>
                            </ul>
                        </details>
                    </li>
                    <li class="dir">
                        <details open>
                            <summary>
                                <a class="deadlink">
                                    Virtualization
                                </a>
                                <a class="pagenav" href="/core_concepts/virtualization/virtualization/virtualization.md">
                                    (page)
                                </a>
                            </summary>
                            <ul>
                                <ul>
                                    <li class="fil">
                                        <a href="/core_concepts/virtualization/esxi.md">
                                            Esxi
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/virtualization/hypervisor.md">
                                            Hypervisor
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/virtualization/kubernetes.md">
                                            Kubernetes
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/virtualization/nutanix.md">
                                            Nutanix
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/virtualization/proxmox.md">
                                            Proxmox
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/virtualization/truenas.md">
                                            Truenas
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/virtualization/unraid.md">
                                            Unraid
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/virtualization/virtualbox.md">
                                            Virtualbox
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/virtualization/vmware_workstation.md">
                                            Vmware Workstation
                                        </a>
                                    </li>
                                </ul>
                            </ul>
                        </details>
                    </li>
                    <li class="dir">
                        <details open>
                            <summary>
                                <a class="deadlink">
                                    Web
                                </a>
                                <a class="pagenav" href="/core_concepts/web/web/web.md">
                                    (page)
                                </a>
                            </summary>
                            <ul>
                                <ul>
                                    <li class="dir">
                                        <details>
                                            <summary>
                                                <a class="deadlink">
                                                    Web Applications
                                                </a>
                                                <a class="pagenav" href="/core_concepts/web/web_applications/web_applications/web_applications.md">
                                                    (page)
                                                </a>
                                            </summary>
                                            <ul>
                                                <ul>
                                                    <li class="fil">
                                                        <a href="/core_concepts/web/web_applications/wsgi.md">
                                                            Wsgi
                                                        </a>
                                                    </li>
                                                </ul>
                                            </ul>
                                        </details>
                                    </li>
                                    <li class="dir">
                                        <details>
                                            <summary>
                                                <a class="deadlink">
                                                    Web Servers
                                                </a>
                                                <a class="pagenav" href="/core_concepts/web/web_servers/web_servers/web_servers.md">
                                                    (page)
                                                </a>
                                            </summary>
                                            <ul>
                                                <ul>
                                                    <li class="fil">
                                                        <a href="/core_concepts/web/web_servers/nginx.md">
                                                            Nginx
                                                        </a>
                                                    </li>
                                                    <li class="fil">
                                                        <a href="/core_concepts/web/web_servers/wsgi_hosting.md">
                                                            Wsgi Hosting
                                                        </a>
                                                    </li>
                                                </ul>
                                            </ul>
                                        </details>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/web/grpc.md">
                                            Grpc
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/web/http.md">
                                            Http
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/web/rest.md">
                                            Rest
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/core_concepts/web/web_servers.md">
                                            Web Servers
                                        </a>
                                    </li>
                                </ul>
                            </ul>
                        </details>
                    </li>
                </ul>
            </ul>
        </details>
    </li>
    <li class="dir">
        <details open>
            <summary>
                <a class="deadlink">
                    Dev Tips
                </a>
                <a class="pagenav" href="/dev_tips/dev_tips/dev_tips.md">
                    (page)
                </a>
            </summary>
            <ul>
                <ul>
                    <li class="dir">
                        <details open>
                            <summary>
                                <a class="deadlink">
                                    Pictures
                                </a>
                                <a class="pagenav" href="/dev_tips/pictures/pictures/pictures.md">
                                    (page)
                                </a>
                            </summary>
                            <ul>
                                <ul></ul>
                            </ul>
                        </details>
                    </li>
                    <li class="fil">
                        <a href="/dev_tips/multi_line_editing.md">
                            Multi Line Editing
                        </a>
                    </li>
                    <li class="fil">
                        <a href="/dev_tips/regex_find_and_replace.md">
                            Regex Find And Replace
                        </a>
                    </li>
                </ul>
            </ul>
        </details>
    </li>
    <li class="dir">
        <details open>
            <summary>
                <a class="deadlink">
                    K8s New
                </a>
                <a class="pagenav" href="/k8s_new/k8s_new/k8s_new.md">
                    (page)
                </a>
            </summary>
            <ul>
                <ul>
                    <li class="fil">
                        <a href="/k8s_new/helm.md">
                            Helm
                        </a>
                    </li>
                    <li class="fil">
                        <a href="/k8s_new/install.md">
                            Install
                        </a>
                    </li>
                    <li class="fil">
                        <a href="/k8s_new/mongo.md">
                            Mongo
                        </a>
                    </li>
                </ul>
            </ul>
        </details>
    </li>
    <li class="dir">
        <details open>
            <summary>
                <a class="deadlink">
                    Laser Distance Module
                </a>
                <a class="pagenav" href="/laser_distance_module/laser_distance_module/laser_distance_module.md">
                    (page)
                </a>
            </summary>
            <ul>
                <ul>
                    <li class="fil">
                        <a href="/laser_distance_module/assembly.md">
                            Assembly
                        </a>
                    </li>
                    <li class="fil">
                        <a href="/laser_distance_module/parts.md">
                            Parts
                        </a>
                    </li>
                </ul>
            </ul>
        </details>
    </li>
    <li class="dir">
        <details open>
            <summary>
                <a class="deadlink">
                    Motorcycles
                </a>
                <a class="pagenav" href="/motorcycles/motorcycles/motorcycles.md">
                    (page)
                </a>
            </summary>
            <ul>
                <ul>
                    <li class="dir">
                        <details open>
                            <summary>
                                <a class="deadlink">
                                    696
                                </a>
                                <a class="pagenav" href="/motorcycles/696/696/696.md">
                                    (page)
                                </a>
                            </summary>
                            <ul>
                                <ul>
                                    <li class="fil">
                                        <a href="/motorcycles/696/parts.md">
                                            Parts
                                        </a>
                                    </li>
                                </ul>
                            </ul>
                        </details>
                    </li>
                    <li class="dir">
                        <details open>
                            <summary>
                                <a class="deadlink">
                                    Ducati
                                </a>
                                <a class="pagenav" href="/motorcycles/Ducati/Ducati/Ducati.md">
                                    (page)
                                </a>
                            </summary>
                            <ul>
                                <ul>
                                    <li class="fil">
                                        <a href="/motorcycles/Ducati/readme.md">
                                            Readme
                                        </a>
                                    </li>
                                </ul>
                            </ul>
                        </details>
                    </li>
                    <li class="dir">
                        <details open>
                            <summary>
                                <a class="deadlink">
                                    S4r
                                </a>
                                <a class="pagenav" href="/motorcycles/s4r/s4r/s4r.md">
                                    (page)
                                </a>
                            </summary>
                            <ul>
                                <ul>
                                    <li class="fil">
                                        <a href="/motorcycles/s4r/parts.md">
                                            Parts
                                        </a>
                                    </li>
                                </ul>
                            </ul>
                        </details>
                    </li>
                    <li class="fil">
                        <a href="/motorcycles/general.md">
                            General
                        </a>
                    </li>
                    <li class="fil">
                        <a href="/motorcycles/monster_696.md">
                            Monster 696
                        </a>
                    </li>
                    <li class="fil">
                        <a href="/motorcycles/monster_s4r.md">
                            Monster S4r
                        </a>
                    </li>
                </ul>
            </ul>
        </details>
    </li>
    <li class="dir">
        <details open>
            <summary>
                <a class="deadlink">
                    Unsorted
                </a>
                <a class="pagenav" href="/unsorted/unsorted/unsorted.md">
                    (page)
                </a>
            </summary>
            <ul>
                <ul>
                    <li class="dir">
                        <details open>
                            <summary>
                                <a class="deadlink">
                                    Camera
                                </a>
                                <a class="pagenav" href="/unsorted/camera/camera/camera.md">
                                    (page)
                                </a>
                            </summary>
                            <ul>
                                <ul>
                                    <li class="dir">
                                        <details>
                                            <summary>
                                                <a class="deadlink">
                                                    Gps Integration
                                                </a>
                                                <a class="pagenav" href="/unsorted/camera/gps-integration/gps-integration/gps-integration.md">
                                                    (page)
                                                </a>
                                            </summary>
                                            <ul>
                                                <ul></ul>
                                            </ul>
                                        </details>
                                    </li>
                                    <li class="fil">
                                        <a href="/unsorted/camera/gps-integration.md">
                                            Gps Integration
                                        </a>
                                    </li>
                                </ul>
                            </ul>
                        </details>
                    </li>
                    <li class="dir">
                        <details open>
                            <summary>
                                <a class="deadlink">
                                    Claude Ai Camera App
                                </a>
                                <a class="pagenav" href="/unsorted/claude-ai-camera-app/claude-ai-camera-app/claude-ai-camera-app.md">
                                    (page)
                                </a>
                            </summary>
                            <ul>
                                <ul>
                                    <li class="fil">
                                        <a href="/unsorted/claude-ai-camera-app/readme.md">
                                            Readme
                                        </a>
                                    </li>
                                </ul>
                            </ul>
                        </details>
                    </li>
                    <li class="dir">
                        <details open>
                            <summary>
                                <a class="deadlink">
                                    Rpi Pico
                                </a>
                                <a class="pagenav" href="/unsorted/rpi-pico/rpi-pico/rpi-pico.md">
                                    (page)
                                </a>
                            </summary>
                            <ul>
                                <ul>
                                    <li class="fil">
                                        <a href="/unsorted/rpi-pico/rpi-pico.md">
                                            Rpi Pico
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/unsorted/rpi-pico/rpi-pico_gps-serial.md">
                                            Rpi Pico Gps Serial
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/unsorted/rpi-pico/rpi-pico_micropython-serial-communication.md">
                                            Rpi Pico Micropython Serial Communication
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/unsorted/rpi-pico/rpi-pico_serial-communication-via-usb.md">
                                            Rpi Pico Serial Communication Via Usb
                                        </a>
                                    </li>
                                    <li class="fil">
                                        <a href="/unsorted/rpi-pico/rpi-pico_usb-device-mode.md">
                                            Rpi Pico Usb Device Mode
                                        </a>
                                    </li>
                                </ul>
                            </ul>
                        </details>
                    </li>
                    <li class="fil">
                        <a href="/unsorted/3.5-in-display.md">
                            3 5 In Display
                        </a>
                    </li>
                    <li class="fil">
                        <a href="/unsorted/i2c-display.md">
                            I2c Display
                        </a>
                    </li>
                    <li class="fil">
                        <a href="/unsorted/imu.md">
                            Imu
                        </a>
                    </li>
                    <li class="fil">
                        <a href="/unsorted/no_driver.md">
                            No Driver
                        </a>
                    </li>
                    <li class="fil">
                        <a href="/unsorted/rpi-ups.md">
                            Rpi Ups
                        </a>
                    </li>
                    <li class="fil">
                        <a href="/unsorted/spi_display_help.md">
                            Spi Display Help
                        </a>
                    </li>
                    <li class="fil">
                        <a href="/unsorted/tof-sensor.md">
                            Tof Sensor
                        </a>
                    </li>
                </ul>
            </ul>
        </details>
    </li>
    <li class="fil">
        <a href="/Home.md">
            Home
        </a>
    </li>
    <li class="fil">
        <a href="/sidebar.md">
            Sidebar
        </a>
    </li>
</ul>