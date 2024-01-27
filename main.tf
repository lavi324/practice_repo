provider "helm" {
  kubernetes {
    config_path = "~/.kube/config"
  }
}

# Install Helm chart into the "mongo" namespace
resource "helm_release" "mongo_enterprise_operator" {
  chart      = "enterprise-operator"
  repository = "https://mongodb.github.io/helm-charts"
  version    = "1.24.0"
  name       = "mongo-enterprise-operator"
  namespace  = "mongo"
  # Other configuration options as needed