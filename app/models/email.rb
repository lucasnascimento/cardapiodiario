class Email
  include Mongoid::Document
  field :email, type: String
  field :name, type: String
  field :status, type: String
  belongs_to :restaurant
end
