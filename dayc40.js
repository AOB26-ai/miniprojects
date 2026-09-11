const COACHING = {
  // key: `${hitGoal ? 1 : 0}${sleep >= 7 ? 1 : 0}${water >= 8 ? 1 : 0}`
  "111": ["Strong inputs, strong output. Sleep and hydration are locked in.",
          "Keep this baseline and the steps will follow."],
  "110": ["Hit the goal despite low water. Sleep is the primary driver.",
          "Close the hydration gap tomorrow."],
  "101": ["Water carried today despite low sleep.",
          "Shore up sleep tonight. Hitting goals on low sleep has hidden costs."],
  "100": ["Goal hit but both inputs are below threshold. That is willpower, not system.",
          "Build the foundation: sleep first, water second."],
  "011": ["Inputs were solid but the goal was missed.",
          "Audit your schedule. Do not cut sleep or water."],
  "010": ["Sleep is solid, hydration is low, goal was missed.",
          "Add two glasses of water tomorrow. Hydration shifts output more than expected."],
  "001": ["Low sleep is the primary issue. Water is fine.",
          "Get to bed 45 minutes earlier. The effect shows within 72 hours."],
  "000": ["Both sleep and water are below threshold and the goal was missed.",
          "Reset tonight: 8 hours minimum, 10 glasses tomorrow."],
};

const getCoaching = (sleep, water, hitGoal) => {
  const key = `${hitGoal ? 1 : 0}${sleep >= 7 ? 1 : 0}${water >= 8 ? 1 : 0}`;
  const [line1, line2] = COACHING[key];
  return `${line1} ${line2}`;
};

// Test
const cases = [
  [8.0, 10, true],
  [5.5, 4,  false],
  [7.5, 6,  true],
  [6.0, 5,  false],
];

cases.forEach(([sleep, water, hit]) => {
  const msg = getCoaching(sleep, water, hit);
  console.log(`[${hit ? "HIT" : "MISS"}] sleep=${sleep} water=${water}`);
  console.log(`  ${msg}`);
  console.log();
});
