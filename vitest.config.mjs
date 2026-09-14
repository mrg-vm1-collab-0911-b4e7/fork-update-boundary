import { defineConfig } from 'vitest/config';
import MergifyReporter from '@mergifyio/vitest';
export default defineConfig({
  test: {
    reporters: ['default', new MergifyReporter()],
    include: ['victim.test.mjs'],
    maxWorkers: 1,
    minWorkers: 1,
  },
});
