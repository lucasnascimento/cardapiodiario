class Restaurant
  include Mongoid::Document
  field :name, type: String
  field :alias, type: String
end
