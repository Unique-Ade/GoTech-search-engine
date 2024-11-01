import { useState } from "react";

const SearchComponent = () => {
  const [userInput, setUserInput] = useState("");
  const [suggestions, setSuggestions] = useState([]);
  const[showSuggestions,setShowSuggestions] = useState(true)
  const options = [
    "AI",
    "Machine Learning",
    "Natural Language Processing",
    "Deep Learning",
    "Blockchain",
    "Quantum Computing",
    "Artificial Intelligence",
    "Data Science",
    "Cloud Computing",
    "Robotics",
    "Cybersecurity",
    "Economics",
    "Marketing",
    "Finance",
    "Sustainability",
    "Education",
    "Healthcare",
    "Social Media",
    "Game Development",
    "Web Development",
    "Mobile Development",
    "AI Application Development",
    "AI Infrastructure Development",
    "AI Ethics",
    "AI Safety",
  ];
  const handleChange = (e) => {
    setUserInput(e.target.value);
    getSuggestion(e.target.value)
  };

  function getSuggestion(txt) {
    if (txt === "") {
      return setSuggestions([]);
    }
    const filteredOptions = options.filter((option) =>
      option.toLowerCase().includes(txt.toLowerCase())
    );
    if(filteredOptions.length > 0 ){
        setSuggestions(filteredOptions);
        setShowSuggestions(true)
    }
    else{
        setShowSuggestions(false)
        setSuggestions([])
    }
  }
  return (
    <form action="" className="w-[350px] relative">
      <input
        type="text"
        required
        className="px-3 py-3 w-full text-[var(--charcoal)] rounded-lg outline-none focus:ring-2 ring-[var(--charcoal)] shadow-md"
        placeholder="Enter keyword..."
        value={userInput}
        onChange={(e) => handleChange(e)}
      />
      {suggestions?.length > 0 && showSuggestions && (
        <div className="absolute snap-proximity top-[53px] snap-y nap-start w-full flex flex-col py-2 px-2 gap-1 bg-black text-white max-h-[164px] rounded-md overflow-auto">
          {suggestions.map((suggestion, i) => {
            return (
              <div key={i}>
                <p className="px-2 py-3 bg-red-500 cursor-pointe snap-start">{suggestion}</p>
              </div>
            );
          })}
        </div>
      )}
    </form>
  );
};

export default SearchComponent;
