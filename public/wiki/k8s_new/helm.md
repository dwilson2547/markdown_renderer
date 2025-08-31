helm repo add 
helm dependency update ./module/helm

helm template --values ./overrides.yaml --values ./overrides.json ./module/helm > manifest.yaml

