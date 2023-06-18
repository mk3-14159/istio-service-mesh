<div align="center">
  <a href="https://github.com/karchuntan/service-mesh-istio">
    <img src="https://cdn1.iconfinder.com/data/icons/navigation-line-4/64/navigation-14-512.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Service Mesh: Tracing of Microservices application</h3>

  <p align="center">
    A small micro-innovation project
    <br /><br />
    <a href="https://github.com/karchuntan/istio-service-mesh/issues">Report Bug</a>
    ·
    <a href="https://github.com/karchuntan/istio-service-mesh/issues">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#suggestion">Suggestion</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

Nowadays, many companies like to adopt microservice approach to perform their business operations. The modular microservice approach provides a greater flexibility and durability, which enables developers to develop these applications faster.

But, it also comes with some challenges and complexity when having many microservices applications;

- Embedding or implementing all the different requirements (Authentication, Logging, …) into each microservice
- Complex service networking
- Security
- Observability
- A lot of pods and many abstraction layers
- When the application receives heavy traffic, a microservice app might become overwhelmed if it receives too many requests too quickly.


<!-- BUILT WITH -->
## Built With

* [Python 3.11](https://www.python.org/)
* [Docker](https://www.docker.com/)
* [Dockerhub](https://hub.docker.com/)
* [Kubernetes](https://kubernetes.io/)
  * [k3s](https://k3s.io/)
* [Istio](https://istio.io/)


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Install Kubernetes cluster

### Suggestion

You can follow this sequence: `default -> delay -> abort -> circuit-breaking`

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/karchuntan/istio-service-mesh.git
   ```

2. Change directory
   ```sh
    cd istio-service-mesh/
   ```

3. Refer this [Istio documentation](https://istio.io/latest/docs/setup/getting-started/) to download and install Istio

4. Apply manifest files
   ```sh
   kubectl apply -f manifests/
   ```

5. Analyze istioctl configuration contain any issues
   ```sh
   istioctl analyze
   ```

6. Determine your [Ingress Host and Port](https://istio.io/latest/docs/setup/getting-started/#determining-the-ingress-ip-and-ports)
   - Ingress Host: I'm using **IP address** in this case, starting from `192.168.*.*`
   - Ingress Port: I'm using **nodePort** in this case

7. Send requests to service
   ```bash
   # Sample test
   while true; do curl -s --noproxy '*' -HHost:kc.employee.com http://192.168.122.69:30282; sleep 1; done

   # Headers
   while true; do curl -I -s --noproxy '*' -H 'position:manager' -HHost:kc.employee.com http://192.168.122.69:30282; sleep 1; done

   # A/B testing and Canary Deployment
   while true; do curl -s --noproxy '*' -HHost:kc.employee.com http://192.168.122.69:30282 | grep 'opacity-75 text-' | head -n1; sleep 1; done

   # circuit breaking
   hey -n 100 -c 50 -m GET -H "Host: kc.employee.com" -host "kc.employee.com" http://192.168.122.69:30282/home
   ```
    - If got proxy, remember to bypass it through `--noproxy '*'`
    - No need to register your IP in `/etc/hosts` file
    - You can also install [hey](https://github.com/rakyll/hey) to test for your circuit breaking


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact

[Kar Chun Tan](karchuntan.1999@gmail.com)
