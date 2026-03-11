// Task 2: use database
use bookstore

// Task 3: insert first author
db.authors.insertOne({
  name: "Jane Austen",
  nationality: "British",
  bio: {
    short: "English novelist known for novels about the British landed gentry.",
    long: "Jane Austen was an English novelist whose works critique and comment upon the British landed gentry at the end of the 18th century."
  }
})

// Task 4: update to add birthday
db.authors.updateOne(
  { name: "Jane Austen" },
  { $set: { birthday: "1775-12-16" } }
)

// Task 5: insert four more authors
db.authors.insertMany([
  {
    name: "L. M. Montgomery",
    nationality: "Canadian",
    bio: {
      short: "Montgomery is an author best known for Anne of Green Gables.",
      long: "Lucy Maud Montgomery was a Canadian novelist who is most known for the Anne of Green Gables series which became a beloved work in children's literature."
    },
    birthday: "1874-11-30"
  },
  {
    name: "Suzanne Collins",
    nationality: "American",
    bio: {
      short: "Suzanne Collins is an author best known for The Hunger Games.",
      long: "Suzanne Collins is an American TV writer and novelist best known for The Hunger Games trilogy, a popular dystopian YA series."
    },
    birthday: "1962-08-10"
  },
  {
    name: "Mo Yan",
    nationality: "Chinese",
    bio: {
      short: "Mo Yan is a novelist and Nobel Prize winner.",
      long: "Mo Yan is a Chinese novelist who won the 2012 Nobel Prize in Literature and is best known for works such as Red Sorghum."
    },
    birthday: "1955-02-17"
  },
  {
    name: "Haruki Murakami",
    nationality: "Japanese",
    bio: {
      short: "Haruki Murakami is an author best known for magical realist fiction.",
      long: "Haruki Murakami is an internationally acclaimed Japanese novelist known for works such as Norwegian Wood, Kafka on the Shore, and 1Q84."
    },
    birthday: "1949-01-12"
  }
])

// Task 6: total count
db.authors.countDocuments({})

// Task 7: British authors, sorted by name
db.authors.find({ nationality: "British" }).sort({ name: 1 })
