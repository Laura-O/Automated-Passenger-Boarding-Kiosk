resource "random_string" "random" {
  length  = 12
  upper   = false
  special = false
}

resource "azurerm_resource_group" "rg" {
  name     = "${var.name}-rg"
  location = var.location
}

resource "azurerm_storage_account" "sa" {
  name                     = "${var.name}storage"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "GRS"

  blob_properties {
    cors_rule {
      allowed_headers    = ["*"]
      allowed_methods    = ["DELETE", "GET", "HEAD", "MERGE", "POST", "OPTIONS", "PUT", "PATCH"]
      allowed_origins    = ["https://fott-2-1.azurewebsites.net/"]
      exposed_headers    = ["*"]
      max_age_in_seconds = 0
    }
  }

  tags = {
  }
}

resource "azurerm_cognitive_account" "fr" {
  name                = "${var.name}fr"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  kind                = "FormRecognizer"

  sku_name = "F0"

  tags = {
  }
}

resource "azurerm_cognitive_account" "face" {
  name                = "${var.name}face"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  kind                = "Face"

  sku_name = "F0"

  tags = {
  }
}

resource "azurerm_media_services_account" "mediaservices" {
  name                = "udacityproject1medias"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  storage_account {
    id         = azurerm_storage_account.sa.id
    is_primary = true
  }
}

resource "azurerm_cognitive_account" "cvtraining" {
  name                = "${var.name}cvtraining"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  kind                = "CustomVision.Training"

  sku_name = "S0"
}

resource "azurerm_cognitive_account" "cvtesting" {
  name                = "${var.name}cvtesting"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  kind                = "CustomVision.Prediction"

  sku_name = "S0"
}
