const SearchComponent = () => {
    return (
        <form>
            <input type="text" placeholder="Search..." />
            <button type="submit">Search</button>
            <div className="results">
                <h2>Results</h2>
                {/* Display search results */}
            </div>
        </form>
    );
}
 
export default SearchComponent;