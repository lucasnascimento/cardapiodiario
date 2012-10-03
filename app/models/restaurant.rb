class Restaurant
  include Mongoid::Document
  field :name, type: String
  field :alias, type: String
  has_many :emails
end
