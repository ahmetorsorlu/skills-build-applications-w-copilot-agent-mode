import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
    console.log('Workouts API endpoint:', apiUrl);
    
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return (
    <div className="container mt-4">
      <div className="loading-spinner">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
      </div>
    </div>
  );
  
  if (error) return (
    <div className="container mt-4">
      <div className="error-message">
        <strong>Error:</strong> {error}
      </div>
    </div>
  );

  return (
    <div className="container mt-4">
      <h2>💪 Workout Suggestions</h2>
      <p className="text-muted mb-4">Personalized workout recommendations for all fitness levels</p>
      <div className="row">
        {workouts.length > 0 ? (
          workouts.map((workout, index) => (
            <div key={workout.id || index} className="col-md-6 mb-4">
              <div className="card h-100">
                <div className="card-body">
                  <h5 className="card-title">{workout.name}</h5>
                  <p className="card-text text-muted">{workout.description}</p>
                  <hr />
                  <ul className="list-group list-group-flush">
                    <li className="list-group-item">
                      <strong>Type:</strong> <span className="badge bg-primary">{workout.workout_type}</span>
                    </li>
                    <li className="list-group-item">
                      <strong>Difficulty:</strong> <span className="badge bg-warning text-dark">{workout.difficulty_level}</span>
                    </li>
                    <li className="list-group-item">
                      <strong>Duration:</strong> {workout.duration} minutes
                    </li>
                    <li className="list-group-item">
                      <strong>Calories:</strong> <span className="badge bg-success">{workout.estimated_calories} kcal</span>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <p className="text-center text-muted">No workout suggestions found</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default Workouts;
